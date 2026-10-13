# Keeping the manuscript and catalogue aligned

The project-page PDF is the latest accepted author revision. The arXiv link identifies the official arXiv record; publishing here does not submit an arXiv replacement. `docs/assets/manuscript-release.json` records the author-revision date, counts and exact artifact hashes.

The living catalogue and manuscript have different scopes. Add only papers whose mechanisms, evidence or evaluation inform robot in-context learning. Record training-time versus deployment-time changes accurately. Catalogue inclusion does not automatically mean a manuscript citation or fixed-weight ICL.

When publishing an accepted manuscript revision:

1. Copy the accepted PDF and its corresponding Figure 9 exports and Supplement S1. Preserve the author order, source dates, classification and agreed exclusions.
2. Update both README news entries, project-page PDF links, paper information page, metadata, section-page links and release manifest in the same commit. Keep existing video, layout and unrelated catalogue changes.
3. Check the catalogue entries against the accepted additions by stable paper ID, without duplicating entries. Reconcile the manuscript census with Supplement S1 and Figure 9 using their own denominators.
4. Run `python3 scripts/check_manuscript_release.py`. Visually inspect changed manuscript pages and any changed web layout before publishing.
5. Re-fetch main before a normal fast-forward push. Read back the remote changed files and deployed PDF, and match hashes to the accepted artifacts. Record any remaining deployment delay instead of claiming the live site is current.

For catalogue-only maintenance, preserve the last accepted manuscript snapshot, synchronize the two homepages with their category files, and update `catalogue_works` separately. Do not relabel an unreviewed manuscript as accepted or an author revision as a new arXiv version.

## Star History chart

The chart starts on September 20, 2026, the verified first Star date. The historical seed comes from the public Star History CSV verified on October 13, 2026; subsequent daily totals come directly from the GitHub repository API. Counts are not rebased. Same-day changes replace that day's latest total, including decreases.

`.github/workflows/star-history.yml` refreshes both themes when a new Star arrives (`watch: started`), with an hourly scheduled reconciliation and manual dispatch. GitHub Actions queues and image caching can delay visible updates. Scheduled workflows may be disabled by GitHub after prolonged repository inactivity; resume them from the Actions tab if needed.

The workflow commits only generated charts and aggregate `history.json` to the dedicated `star-history` branch. Both README files embed that branch. It uses the repository's short-lived `GITHUB_TOKEN` with contents-write permission; no personal token or change to main's protection is needed. Failed API calls leave the published charts unchanged. Inspect the Refresh Star History workflow runs for failures.
