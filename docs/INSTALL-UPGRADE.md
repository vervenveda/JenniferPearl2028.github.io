# Install the Jennifer Pearl 2028 Gateway Upgrade

This is an **additive package**. It does not overwrite `index.html` or remove any existing files.

## Before upload

1. Open the repository: https://github.com/vervenveda/JenniferPearl2028.github.io
2. Download a backup of the current repository or confirm the latest commit can be restored.
3. Unzip this package on your computer.
4. Inspect the included files before uploading.

## Files to add

Copy these paths from the ZIP into the repository root, preserving directory names:

- `BASELINE-AUDIT.md`
- `docs/INSTALL-UPGRADE.md`
- `docs/UPGRADE-ROADMAP.md`
- `tools/check_site.py`
- `.github/workflows/site-quality.yml`

Do not upload the outer `JenniferPearl2028_gateway_upgrade` folder itself; upload its contents so `.github`, `docs`, and `tools` sit at the repository root.

## Upload through GitHub's web interface

1. Open the repository's **Add file** menu and choose **Upload files**.
2. Upload the listed files, retaining their directory structure. If the browser upload interface does not preserve nested directories, create each folder and file using **Add file → Create new file**.
3. Review the change list. Confirm `index.html` is unchanged.
4. Commit with a message such as: `Add repeatable gateway quality checks`.
5. Open the **Actions** tab and inspect the `Gateway quality checks` workflow run.
6. If the workflow fails, open the log and correct the reported local HTML structure issues before merging more changes.

## Run the checker locally

Requires Python 3.9+ and no third-party packages.

```bash
python3 tools/check_site.py
```

The checker scans HTML files in the repository, checking duplicate IDs, empty links, broken local fragment references, and image elements without an `alt` attribute. It also flags HTML pages without a title. It does not fetch external links.

## Rollback

If the workflow or checker causes an unwanted failure, remove `.github/workflows/site-quality.yml` and `tools/check_site.py` or revert the commit. The existing site page is not modified by this package.

## Important limitations

- GitHub Actions runs only after these files are uploaded and committed.
- A passing structural check does not prove that external websites work or that a site conforms to WCAG.
- Do not add campaign forms, donations, accounts, analytics, or personal-data collection as part of this package without a separate implementation and compliance review.
