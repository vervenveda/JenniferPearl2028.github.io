# Upgrade Roadmap — Gateway Repository

## Phase 1 — Baseline and repeatable checks (included in this package)

- Record current behavior and known risks.
- Add dependency-free local HTML checks.
- Run checks automatically on pushes and pull requests.
- Preserve the current homepage and existing resource links.

## Phase 2 — Link and deployment verification

- Test each outbound destination and record final URL, HTTP status, redirect chain, and expected page.
- Check fragment links after redirects.
- Inspect GitHub Pages settings and workflow history.
- Verify the deployed page reflects the intended repository commit.
- Treat transient network failures separately from confirmed broken destinations.

## Phase 3 — Accessibility and responsive behavior

- Keyboard-only test: skip link, menu open/close, Escape, focus order, and destination focus.
- Screen-reader check: page title, landmarks, navigation labels, link names, and status messages.
- Contrast and focus-visibility review against WCAG 2.2 AA criteria.
- Test widths around 320, 390, 768, 1024, and 1440 CSS pixels.
- Check browser zoom to 200% and reduced-motion settings.

## Phase 4 — Performance and security review

- Capture Lighthouse or equivalent performance/accessibility/SEO results from the live page.
- Inspect image sizes, render-blocking resources, cache behavior, and layout shifts.
- Confirm whether the external `vnv-beta-link.js` script is needed and what it changes.
- Review third-party requests and any analytics/cookie behavior.
- Avoid adding unnecessary dependencies; consider a Content Security Policy only after enumerating every legitimate external resource.

## Phase 5 — Campaign website audit (separate scope)

Audit `https://jenniferpearl2028.github.io/` separately. Review its page structure, policy and biography content, contact pathways, campaign disclaimers where applicable, privacy practices, accessibility, performance, and deployment configuration. Do not infer that the gateway audit validates the campaign site.
