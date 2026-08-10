/* Redirect source-style Question URLs served through the GitHub Pages 404 page. */
(function legacyQuestionRedirect(global, document) {
  "use strict";

  function normalizedBasePath(basePath) {
    if (!basePath || basePath === "/") {
      return "";
    }

    return `/${basePath.replace(/^\/+|\/+$/g, "")}`;
  }

  function questionHtmlTarget(pathname, search, hash, basePath) {
    const questionPrefix = `${normalizedBasePath(basePath)}/questions/`;

    if (!pathname.startsWith(questionPrefix) || !pathname.endsWith(".md")) {
      return null;
    }

    const questionPath = pathname.slice(questionPrefix.length, -3);
    const segments = questionPath.split("/");
    if (!questionPath || segments.some((segment) => !segment || segment === "." || segment === "..")) {
      return null;
    }

    return `${questionPrefix}${questionPath}.html${search || ""}${hash || ""}`;
  }

  global.LegacyQuestionRedirect = { questionHtmlTarget };

  const script = document && document.currentScript;
  const location = global.location;
  if (!location || typeof location.replace !== "function") {
    return;
  }

  const target = questionHtmlTarget(
    location.pathname,
    location.search,
    location.hash,
    script && script.dataset ? script.dataset.basePath : "",
  );
  if (target) {
    location.replace(target);
  }
})(window, document);
