---
title: Keep Backstage UI customizations upgradable
theme: backend-architecture
difficulty: staff
type: scenario
tags: [architecture, platform-engineering, change-management, quality, governance]
sources:
  - url: https://backstage.io/docs/conf/user-interface
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://backstage.io/docs/getting-started/keeping-backstage-updated
    source_type: official-docs
    verified_on: 2026-08-12
---

# Keep Backstage UI customizations upgradable

Leadership wants the developer portal to carry the company's brand and a
redesigned landing page, and a designer has already sent React components. Your
portal is a Backstage app your team maintains and upgrades. How would you take
the customization work without making every future upgrade painful?

## Answer guide

- Set a rule about where customization is allowed to live before any code lands: theme tokens and app composition are yours to own, upstream component internals are not. In practice that means expressing brand as a theme rather than as edits to plugin components, keeping the designer's components in your own app package, and treating any change that requires copying upstream source as a decision that needs a reason and a follow-up issue.
- The supported mechanism for look and feel is `createUnifiedTheme` from `@backstage/theme`, extended from the base theme options: palette, typography, spacing, shape, page themes, and targeted style overrides through the `components` key. Themes are registered in the app's `App.tsx` with an id, title, light or dark variant, icon, and a provider, so several themes can coexist and users can pick one. The app is a React application built on Material UI, and a new Backstage UI component set is being introduced alongside it, which means during the transition a complete brand has to be expressed in both systems.
- Constraints worth stating up front: theme overrides reach into component styling, so they are coupled to the component structure of the version you wrote them against and can break on a minor upgrade even though nothing in your code changed. Material UI's own major version moves have needed specific handling in Backstage — the class-name prefix setup for v5 is the documented example — and Backstage publishes upgrade guidance and tooling precisely because an app is a repository you maintain, not a product you install. Budget upgrades as recurring work rather than as a project.
- What goes wrong: a portal pinned to an old release because every upgrade breaks a forked component, so plugins and security fixes stop arriving; a brand that only covers half the UI because the second component system was never themed; overrides written per page that drift into an unmaintainable style sheet; and a redesign that removes the affordances plugin authors rely on, so third-party plugins render awkwardly and teams conclude the portal is broken.

## References

- [Backstage: customizing your app's UI](https://backstage.io/docs/conf/user-interface)
- [Backstage: keeping Backstage updated](https://backstage.io/docs/getting-started/keeping-backstage-updated)
- Further reading (blog): [Kosli — customizing the look and feel of Backstage](https://www.kosli.com/blog/succeeding-with-backstage-part-1-customizing-the-look-and-feel-of-backstage/)

## What to learn next

- Official documentation: [Backstage: creating a custom theme](https://backstage.io/docs/getting-started/app-custom-theme)
- Manual or specification: [Material UI theming](https://mui.com/material-ui/customization/theming/)
- Maintainer or personal blog: [Backstage Wrapped 2025](https://backstage.io/blog/2025/12/30/backstage-wrapped-2025)
- Technical blog: [Frontside — using your company's component library with Backstage](https://frontside.com/blog/2022-02-14-component-library-backstage/)
- Hands-on guide: [Backstage: migrating frontend plugins](https://backstage.io/docs/frontend-system/building-plugins/migrating/)
