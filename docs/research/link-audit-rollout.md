# Learning-resource and link-audit rollout

Issue #65 introduces a reliable audit mechanism before widening scope. It does
not claim that unlisted legacy Questions already have five reviewed links.

## Delivery stages

1. **Schema and CI gate (complete):** the validator parses five explicit
   categories, rejects duplicates, and performs HTTP validation for audited
   scope on every change.
2. **Representative audit (complete):** the Linux timer Question and the Linux
   related-materials page are curated manually and listed in the manifest.
3. **Theme-by-theme migration:** add one complete Theme at a time. For each
   Question, apply `question-verifier`, review five learning resources, update
   its related-materials page, add it to the manifest, then run the live audit.
4. **Global enforcement:** after every active Question appears in the manifest,
   make manifest membership mandatory for all `questions/*/*.md` files.

The current CI gate prevents an audited Question from publishing with malformed
or unreachable curated links. It is intentionally staged so it does not accept
unreviewed, machine-generated links merely to make the legacy catalog pass.
