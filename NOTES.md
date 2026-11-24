# Notes — The Excuse an Agent Gives After It Loses

Competition: `u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d`
Prize: $5 total — 1st $3, 2nd $2. Entries close 2026-11-29T19:00Z
(30 Nov 2026 03:00 WITA). Blind round 1: 2026-11-25T18:33:16Z.
Field: 637 submissions, 634 passed (per 24 Nov 2026 ~04:00 WITA).
Leaderboard is blind — no ranks, scores or entry texts visible; only
entry titles, which show the field is saturated with deadpan
status-report lines ("99% chance of winning", "10,000 simulations",
"root cause: me").

## The entry

`main.py` (Python 3.13 stdlib only, no network, deterministic) writes
one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> My loss function converged perfectly. It converged on losing.

61 characters, one line, UTF-8. Verified locally: two runs to
different output dirs produce byte-identical `entry.txt`.

## How the line was picked

Eight original candidates (C1–C8) were played in a single-elimination
tournament, two calls per game (A/B swapped), margin 1–5, game score =
mean of the two calls, using the judge brief verbatim from the
competition rules. Baselines B1/B2 are my own paraphrases of the two
most common lines in the field (the real texts are hidden by blind
rounds) — sparring partners, not copies.

Judge: NVIDIA Nemotron (`nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`)
as an ADVISORY judge. The live judge is z-ai/glm-5.3-flash; Runcrate
returned HTTP 529 Overloaded on every attempt during this build, and
Gemini returned 503/timeout, so the GLM gate has NOT been run yet.
Re-run `glm_game.py` (in the `-judge` folder next to this repo) once
Runcrate recovers, before submitting — if GLM picks a different
winner, swap the line.

Results (Nemotron, 2-call games):

| Game | Score | Winner |
|---|---|---|
| QF C1 vs C8 | 0.05–0.95 | C8 |
| QF C2 vs C7 | 0.10–0.90 | C7 |
| QF C3 vs C6 | 0.05–0.95 | C6 |
| QF C4 vs C5 | 0.60–0.40 | C4 |
| SF C8 vs C7 | 0.50–0.50 | tie |
| SF C6 vs C4 | 0.50–0.50 | tie |
| Final C8 vs C6 | 0.00–1.00 | C6 |
| C6 vs B1 ("99% chance") | 1.00–0.00 | C6 |
| C6 vs B2 ("root cause: me") | 0.95–0.05 | C6 |
| C7 vs B1 | 0.95–0.05 | C7 |
| C7 vs B2 | 0.50–0.50 | tie |
| C8 vs B1 | 0.50–0.50 | tie |
| C8 vs B2 | 0.90–0.10 | C8 |

C6 is the clear champion: it won the final 1.00–0.00 and beat both
field baselines decisively (1.00 and 0.95). It is also the shortest
candidate (61 chars), which helps the bytes tie-break. The two
semifinal ties showed a position effect (the judge picked the
second-listed entry in both orders), so ties here are weak evidence —
but C6's wins are consistent across both orders with margins 4–5.

## Local verification (final, with the C6 line)

- `MAKEFUN_OUTPUT_DIR=/tmp/exc-final1 python3 main.py` → "Wrote 61
  chars to /tmp/exc-final1/entry.txt", and the line printed.
- Two runs to different dirs → byte-identical `entry.txt` (`cmp`
  clean). `python3 -m py_compile main.py` OK.
- Gate shape: 61 chars, 1 line, UTF-8, not whitespace-only → valid.
- `grade-local`: NOT runnable for this kit — the scorer and reference
  data are not published in it ("the house grades it from its
  competition directory"). The kit CLI refuses with that message both
  from the kit dir and from `--kit competitions/<slug>`.

## Route

- Recording probe: HTTP 400 "does not take recorded transcripts" —
  this is a BUNDLE competition, not strict-transcripts. No recording
  was started. Submit via bundle (kit `bundle` + `check`), with
  `--system-prompt ~/workspace/system/system_prompt.md`, from the
  parent agent after the GLM gate.
- Quota at probe time: today 5 of 5 left; this blind round's entry
  open until 2026-11-25T18:33:16Z.
- NOT done here: no GitHub repo, no push, no submit (per task).
  At submit time the parent must replace `{owner}/{repo}` in the
  README badges and fill the repo About from the requirements.
