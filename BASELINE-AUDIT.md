# Jennifer Pearl 2028 Gateway — Baseline Forensic Audit

**Audit date:** 2026-10-14  
**Repository:** https://github.com/vervenveda/JenniferPearl2028.github.io  
**Scope:** Public repository source and existing repository audit notes.  
**Package type:** Additive, non-destructive quality-control upgrade. This package does not replace `index.html`.

## Executive summary

The current homepage is a static HTML/CSS/JavaScript gateway connecting visitors to the dedicated Jennifer Pearl 2028 site and a collection of Verve N Veda public-service resources. The inspected source includes a responsive layout, semantic page landmarks, a skip link, visible focus styling, reduced-motion handling, a mobile menu with ARIA state, and a built-in structural audit.

The most important near-term upgrade is to make repository checks repeatable without disturbing the existing page. This package adds a dependency-free local structural checker and a GitHub Actions workflow that runs it on pushes and pull requests. It also provides an installation checklist and a remediation roadmap.

## Evidence-based findings

### Existing strengths

1. `index.html` has a document language, viewport metadata, description, title, and theme color.
2. The page uses a skip link to `#main`, a labelled primary navigation, a `main` landmark, labelled footer navigation, and `:focus-visible` styling.
3. CSS includes responsive breakpoints and a `prefers-reduced-motion: reduce` rule.
4. The mobile menu has `aria-expanded` and `aria-controls`, and its JavaScript handles Escape, focus movement, link selection, resize, and click-away.
5. The page clearly describes itself as a gateway and directs campaign-specific information to a separate campaign website.
6. The built-in `auditJenniferPearlGateway()` checks duplicate IDs, blank links, missing local fragment targets, image/media elements, file-upload controls, and campaign-site links.

### Issues and risks to verify

1. **External script dependency:** `index.html` loads `https://vervenveda.com/assets/vnv-beta-link.js`. Verify that the script is still needed, loads reliably, and does not modify page links unexpectedly. This package does not remove it.
2. **Built-in audit scope:** the existing audit does not verify external HTTP destinations, accessibility conformance, security headers, performance metrics, or whether external scripts succeed.
3. **Link freshness:** the gateway links to numerous separate services. Their current availability must be tested independently; a link in source code is not proof that the destination is live.
4. **Prior documented maintenance notes:** the repository's `AUDIT-AND-INSTALL.txt` dated 2026-10-08 records placeholder `.webp` gallery files, empty gallery/validator files, and workflow files placed under `.github/   workflows` (with spaces). Confirm these paths and usages in the repository before deleting or moving anything. This package does not remove them.
5. **Publication status:** the same prior audit records a GitHub update failure with HTTP 403 and says no remote commit was made at that time. Recheck current repository permissions and the live deployment before assuming that any prior local repair was published.
6. **Campaign disclosure:** confirm applicable disclaimer and privacy obligations for the actual campaign website and each communication. This gateway says it does not process contributions or collect campaign data; do not add collection forms without a separate privacy/security review.
7. **Identity and destinations:** verify that every “official campaign site” label points to the destination the campaign intends to designate as official.

## Included upgrades

- `tools/check_site.py`: dependency-free structural checks for local HTML pages.
- `.github/workflows/site-quality.yml`: runs the checker on pushes and pull requests.
- `docs/INSTALL-UPGRADE.md`: installation, rollback, and verification steps.
- `docs/UPGRADE-ROADMAP.md`: sequenced next steps for a deeper production audit.
- `BASELINE-AUDIT.md`: this report.

## What this audit does not claim

- It does not claim every external destination was checked live on 2026-10-14.
- It does not claim a WCAG audit, Lighthouse/Core Web Vitals measurement, security penetration test, or cross-browser test has been completed.
- It does not claim the package has been installed or committed to GitHub.
- It does not replace the dedicated campaign website's own audit.
- It does not modify or replace the current `index.html`.

## Research references

- GitHub Pages setup and publishing behavior: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- GitHub Pages overview: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- W3C accessibility standards: https://www.w3.org/WAI/standards-guidelines/wcag/
- FEC disclaimer guidance: https://www.fec.gov/help-candidates-and-committees/advertising-and-disclaimers/
- Library of Congress U.S. Elections Web Archive: https://www.loc.gov/collections/united-states-elections-web-archive/about-this-collection/

## Initial priority order

1. Add repeatable structural checks (included).
2. Confirm workflow execution and deployment settings after upload.
3. Test all outbound links, including redirects and fragment targets.
4. Test keyboard navigation and screen-reader landmarks at desktop and mobile sizes.
5. Run Lighthouse or equivalent performance measurements on the deployed page.
6. Review external script necessity, privacy, and security.
7. Audit the dedicated campaign site separately.
