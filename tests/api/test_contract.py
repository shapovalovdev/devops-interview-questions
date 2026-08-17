"""Hold the running service to the hand-written API contract.

`api/openapi.yaml` is the source of truth for the wire format, which is only
true if something checks.  This module compares the schema FastAPI generates
from the live routes against the committed contract and fails on any
divergence, so a route cannot quietly grow a parameter, drop a status code,
rename an operation, or appear at a path the contract never promised.

The comparison is deliberately asymmetric, following the epic's rule in
**A complete contract, with stubs marked**:

- *paths, methods, operation ids, tags, parameters, and request bodies* are
  compared for **every** operation, because the contract describes the whole v1
  surface from the day it is written and a stub still has to be reachable at
  the promised address with the promised inputs;
- *response status codes* are compared only for operations marked
  `x-implementation: implemented`, because a stub answers `501` today and its
  documented responses are a promise about a later slice, not a description of
  this build.

What is deliberately **not** compared is the detailed JSON Schema of each
parameter and response body.  FastAPI serializes an optional query parameter as
an `anyOf` with a `title` and a `default`, and forcing the hand-written file to
mirror those artifacts would make the contract a transcript of the framework
rather than a document a client can read.  The dimensions compared here are the
ones a client actually binds to: where an operation lives, what it is called,
what it accepts, and — once implemented — what it can answer.  Enumerated
vocabularies are the exception: when the contract pins an enum (difficulty,
question type, sort key, item kind) the generated schema must pin the same one,
because that vocabulary *is* the interface.
"""

from __future__ import annotations

import unittest
from typing import Any

import yaml

from support import CONTRACT_PATH, demo_app

METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")

IMPLEMENTED = "implemented"
STUB = "stub"
MARKER = "x-implementation"


def load_contract() -> dict[str, Any]:
    return yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8"))


def pointer(reference: str, document: dict[str, Any]) -> Any:
    """Dereference a local JSON pointer such as `#/components/schemas/Question`."""
    assert reference.startswith("#/"), f"only local references are supported: {reference}"
    target: Any = document
    for step in reference[2:].split("/"):
        target = target[step]
    return target


def resolve(node: Any, document: dict[str, Any]) -> Any:
    """Follow a local `$ref` one hop, which is all a parameter list ever needs."""
    if isinstance(node, dict) and "$ref" in node:
        return pointer(node["$ref"], document)
    return node


def operations(document: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    """Every operation in a schema, keyed by `(path, method)`."""
    found: dict[tuple[str, str], dict[str, Any]] = {}
    for path, item in document.get("paths", {}).items():
        for method, operation in item.items():
            if method in METHODS:
                found[(path, method)] = operation
    return found


def parameters(operation: dict[str, Any], document: dict[str, Any]) -> dict[tuple[str, str], bool]:
    """Parameters as `{(name, location): required}`."""
    resolved = [resolve(entry, document) for entry in operation.get("parameters", [])]
    return {(entry["name"], entry["in"]): bool(entry.get("required", False)) for entry in resolved}


def enums(schema: Any, document: dict[str, Any], seen: frozenset[str] = frozenset()) -> list[list[str]]:
    """Every enumerated vocabulary reachable from a schema, references followed.

    Following `$ref` matters: the contract writes `difficulty` as a reference to
    `#/components/schemas/Difficulty`, while FastAPI writes an optional query
    parameter as `anyOf: [{$ref: ...}, {type: null}]`. Comparing the two without
    dereferencing would compare nothing at all and quietly pass.
    """
    found: list[list[str]] = []
    if isinstance(schema, dict):
        reference = schema.get("$ref")
        if isinstance(reference, str) and reference not in seen:
            found.extend(enums(pointer(reference, document), document, seen | {reference}))
        if isinstance(schema.get("enum"), list):
            found.append(sorted(str(value) for value in schema["enum"]))
        for key, value in schema.items():
            if key != "$ref":
                found.extend(enums(value, document, seen))
    elif isinstance(schema, list):
        for value in schema:
            found.extend(enums(value, document, seen))
    return found


def parameter_enums(
    operation: dict[str, Any], document: dict[str, Any]
) -> dict[tuple[str, str], list[list[str]]]:
    """The enumerated vocabulary each parameter pins, where it pins one."""
    pinned: dict[tuple[str, str], list[list[str]]] = {}
    for entry in operation.get("parameters", []):
        entry = resolve(entry, document)
        vocabularies = enums(entry.get("schema", {}), document)
        if vocabularies:
            pinned[(entry["name"], entry["in"])] = sorted(vocabularies)
    return pinned


def request_body(operation: dict[str, Any], document: dict[str, Any]) -> Any:
    """A request body reduced to what a client binds to: media types and schema."""
    body = resolve(operation.get("requestBody"), document)
    if body is None:
        return None
    content = body.get("content", {})
    return {
        "required": bool(body.get("required", False)),
        "media_types": sorted(content),
        "schemas": {
            media: definition.get("schema", {}).get("$ref", "<inline>")
            for media, definition in sorted(content.items())
        },
    }


def statuses(operation: dict[str, Any]) -> set[str]:
    return {str(code) for code in operation.get("responses", {})}


def name(key: tuple[str, str]) -> str:
    path, method = key
    return f"{method.upper()} {path}"


def references(node: Any) -> list[str]:
    """Every `$ref` string anywhere in a document."""
    found: list[str] = []
    if isinstance(node, dict):
        if isinstance(node.get("$ref"), str):
            found.append(node["$ref"])
        for value in node.values():
            found.extend(references(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(references(value))
    return found


def dangling(document: dict[str, Any]) -> list[str]:
    """References the document promises but does not define."""
    broken = []
    for reference in sorted(set(references(document))):
        try:
            pointer(reference, document)
        except (AssertionError, KeyError, TypeError):
            broken.append(reference)
    return broken


class ContractTest(unittest.TestCase):
    """The service and `api/openapi.yaml` must describe the same API."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = load_contract()
        # The application is built here from an explicit store: `api.app:app`
        # resolves its store from the environment, and the shape of the served
        # API does not depend on which store is behind it.
        cls.generated = demo_app().openapi()
        cls.contract_ops = operations(cls.contract)
        cls.generated_ops = operations(cls.generated)

    def test_the_contract_describes_the_whole_v1_surface(self) -> None:
        """A shrunken contract must not be able to make this suite pass."""
        self.assertEqual(
            len(self.contract_ops),
            19,
            "api/openapi.yaml should describe all 19 v1 operations from the epic; "
            f"it describes {sorted(name(key) for key in self.contract_ops)}",
        )

    def test_document_identity_matches(self) -> None:
        """The service must announce the same contract version it is tested against."""
        self.assertEqual(self.contract["openapi"], self.generated["openapi"], "OpenAPI version")
        self.assertEqual(
            self.contract["info"]["title"], self.generated["info"]["title"], "info.title"
        )
        self.assertEqual(
            self.contract["info"]["version"], self.generated["info"]["version"], "info.version"
        )

    def test_both_documents_resolve_every_reference_they_make(self) -> None:
        """A `$ref` to a component nobody defined is a broken document."""
        self.assertFalse(dangling(self.contract), "api/openapi.yaml has dangling references")
        self.assertFalse(dangling(self.generated), "the served schema has dangling references")

    def test_every_operation_declares_its_implementation_state(self) -> None:
        """The marker is what the two tests read; an operation without one is a hole."""
        wrong = {
            name(key): operation.get(MARKER, "<missing>")
            for key, operation in self.contract_ops.items()
            if operation.get(MARKER) not in (IMPLEMENTED, STUB)
        }
        self.assertFalse(
            wrong,
            "every operation in api/openapi.yaml needs "
            f"`{MARKER}: implemented|stub`; wrong or missing on: {wrong}",
        )

    def test_paths_and_methods_match(self) -> None:
        """No route the contract does not promise, and no promise without a route."""
        undocumented = sorted(name(key) for key in self.generated_ops.keys() - self.contract_ops.keys())
        unserved = sorted(name(key) for key in self.contract_ops.keys() - self.generated_ops.keys())
        self.assertFalse(
            undocumented or unserved,
            "the service and api/openapi.yaml disagree on the surface.\n"
            f"  served but not in the contract: {undocumented or 'none'}\n"
            f"  in the contract but not served: {unserved or 'none'}",
        )

    def test_operation_ids_and_tags_match(self) -> None:
        """Client generators key off these, so drift in them breaks every client."""
        divergences: list[str] = []
        for key in sorted(self.contract_ops.keys() & self.generated_ops.keys()):
            documented = self.contract_ops[key]
            served = self.generated_ops[key]
            if documented.get("operationId") != served.get("operationId"):
                divergences.append(
                    f"{name(key)}: operationId is {served.get('operationId')!r} "
                    f"but the contract says {documented.get('operationId')!r}"
                )
            if sorted(documented.get("tags", [])) != sorted(served.get("tags", [])):
                divergences.append(
                    f"{name(key)}: tags are {sorted(served.get('tags', []))} "
                    f"but the contract says {sorted(documented.get('tags', []))}"
                )
        self.assertFalse(divergences, "\n" + "\n".join(divergences))

    def test_parameters_match(self) -> None:
        """Same names, same locations, same required flags, same vocabularies."""
        divergences: list[str] = []
        for key in sorted(self.contract_ops.keys() & self.generated_ops.keys()):
            documented = parameters(self.contract_ops[key], self.contract)
            served = parameters(self.generated_ops[key], self.generated)
            for missing in sorted(documented.keys() - served.keys()):
                divergences.append(f"{name(key)}: contract declares {missing} but the route does not")
            for extra in sorted(served.keys() - documented.keys()):
                divergences.append(f"{name(key)}: route declares {extra} but the contract does not")
            for shared in sorted(documented.keys() & served.keys()):
                if documented[shared] != served[shared]:
                    divergences.append(
                        f"{name(key)}: {shared} is required={served[shared]} on the route "
                        f"but required={documented[shared]} in the contract"
                    )
            documented_enums = parameter_enums(self.contract_ops[key], self.contract)
            served_enums = parameter_enums(self.generated_ops[key], self.generated)
            for parameter, values in sorted(documented_enums.items()):
                if served_enums.get(parameter) != values:
                    divergences.append(
                        f"{name(key)}: {parameter} accepts {served_enums.get(parameter)} "
                        f"but the contract pins {values}"
                    )
        self.assertFalse(divergences, "\n" + "\n".join(divergences))

    def test_request_bodies_match(self) -> None:
        """A body the contract promises must be the body the route parses."""
        divergences: list[str] = []
        for key in sorted(self.contract_ops.keys() & self.generated_ops.keys()):
            documented = request_body(self.contract_ops[key], self.contract)
            served = request_body(self.generated_ops[key], self.generated)
            if documented != served:
                divergences.append(
                    f"{name(key)}: request body is {served} but the contract says {documented}"
                )
        self.assertFalse(divergences, "\n" + "\n".join(divergences))

    def test_response_statuses_match_for_implemented_operations(self) -> None:
        """Only implemented operations owe their documented responses today."""
        divergences: list[str] = []
        for key in sorted(self.contract_ops.keys() & self.generated_ops.keys()):
            if self.contract_ops[key].get(MARKER) != IMPLEMENTED:
                continue
            documented = statuses(self.contract_ops[key])
            served = statuses(self.generated_ops[key])
            if documented != served:
                divergences.append(
                    f"{name(key)}: the route can answer {sorted(served)} "
                    f"but the contract documents {sorted(documented)}"
                )
        self.assertFalse(divergences, "\n" + "\n".join(divergences))

    def test_implemented_operations_never_answer_501(self) -> None:
        """The marker must describe reality, not intention."""
        for key, operation in sorted(self.contract_ops.items()):
            if operation.get(MARKER) == IMPLEMENTED:
                self.assertNotIn(
                    "501",
                    statuses(operation),
                    f"{name(key)} is marked {IMPLEMENTED} yet documents 501",
                )

    def test_contract_documents_no_501(self) -> None:
        """`501` is a fact about this build, carried by the marker, not a promise."""
        offenders = sorted(name(key) for key, op in self.contract_ops.items() if "501" in statuses(op))
        self.assertFalse(
            offenders,
            "501 must not appear in the published contract; "
            f"use `{MARKER}: stub` instead. Found on: {offenders}",
        )


if __name__ == "__main__":
    unittest.main()
