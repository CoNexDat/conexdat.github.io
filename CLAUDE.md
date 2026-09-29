@AGENTS.md

## Claude Code way of working

Every PR is reviewed by a **fresh-context reviewer subagent** before merging:

1. Push the branch, open the PR, and wait for the `Build site` check.
2. Spawn a **new** reviewer with the Agent tool: `model: "sonnet"`,
   `isolation: "worktree"`, and a self-contained prompt with the repository, the PR
   number, `gh pr diff <n>`, the conventions in AGENTS.md, the checks to run (the
   production build with Ruby 3.3, link checks with `curl -sIL` on every added URL, a
   British-spelling scan of English text), "read-only, do not modify the repository",
   and the required output: findings ranked by severity with `file:line`, a concrete
   failing scenario and a suggested fix, ending with exactly `VERDICT: APPROVE` or
   `VERDICT: CHANGES REQUESTED`.
3. Verify each finding before acting on it. Fix it (commit and push) or record in a PR
   comment why it does not apply.
4. After any change, spawn **another fresh** reviewer for the new state; never continue
   the previous reviewer session.
5. Merge only when the check is green on the latest push **and** the latest reviewer
   says `VERDICT: APPROVE`. Post a PR comment summarizing the review rounds, then merge
   with `gh pr merge <n> --squash --delete-branch` and confirm the live site.

The site belongs to the group director, J. Ignacio Alvarez-Hamelin, and is maintained by
Esteban Carisimo. Feedback from the director usually arrives as a list in Spanish; treat
each item as a separate, verifiable fix.
