# Public-launch repository cleanup — 26 November 2026

Liz requested first-name-only attribution, removal of public rehearsal links, cleanup of historical surname occurrences and assignment of the former `a` commits to her repository account.

The current site uses only Liz's first name. The proposal PDF is a redacted public copy; its project text is retained. The display previews are regenerated from editable source. `presentation.html` keeps its bookmark URL and noindex metadata, with no incoming public website links.

History cleanup uses git-filter-repo in a separate clone. Historical text is sanitized, the identified PDF/image blobs are replaced with their verified clean equivalents, and the 26 `a` author/committer identities are mapped to `Liz <287389706+lzl462@users.noreply.github.com>`. The numeric account ID was checked against GitHub's API. Other authors, dates, messages and commit/merge structure are preserved. The public update uses an exact force-with-lease on `main` so a concurrent remote change cannot be silently overwritten. A private recovery copy is kept outside the repository. Existing global Git/SSH/credential configuration is not changed.

## Other working copies after the rewrite

Save any uncommitted/unpublished work outside the old checkout. Create a fresh clone, then transfer only the changes still needed and check them for first-name-only attribution. Do not merge or push the old branch history back into the cleaned repository. Old commit hashes in earlier worklog/review entries refer to the pre-cleanup history.

Rewriting the published branch cannot erase other people's clones, forks or GitHub's cached views of old commits. [GitHub's removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) explains those limits and the separate support process for eligible cached data. No support request or message to another person is sent by this cleanup.
