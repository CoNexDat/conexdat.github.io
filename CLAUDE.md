@AGENTS.md

## Claude Code way of working

Every PR is reviewed by a **fresh-context reviewer subagent** that follows
`.github/REVIEW.md`, before merging:

1. Push the branch, open the PR, and wait for the `Build site` check.
2. Spawn a **new** reviewer with the Agent tool: `model: "sonnet"`,
   `isolation: "worktree"`, and a prompt that says "Follow `.github/REVIEW.md` for PR
   #<n> in CoNexDat/conexdat.github.io" plus anything specific worth testing.
3. Post the reviewer's full verdict on the PR (`gh pr comment <n> --body-file -`).
4. Verify each finding before acting on it. Fix it (commit and push) or reply on the PR
   with the reason it does not apply.
5. After any change, spawn **another fresh** reviewer for the new state; never continue
   the previous reviewer session. It reads the earlier verdicts from the PR comments.
6. Merge only when the check is green on the latest push **and** the latest reviewer
   says `VERDICT: APPROVE`, with `gh pr merge <n> --squash --delete-branch`. Then
   confirm the live site.

Subagent worktrees live under `.claude/worktrees/` (git-ignored). Remove them with
`git worktree remove --force <path>` once the reviewer has reported.

The site belongs to the group director, J. Ignacio Alvarez-Hamelin, and is maintained by
Esteban Carisimo. Feedback from the director usually arrives as a list in Spanish; treat
each item as a separate, verifiable fix.
