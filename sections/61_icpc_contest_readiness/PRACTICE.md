# Practice for Section 61: ICPC Contest Readiness

## External queue

Use these as preparation drills, not as a replacement for full virtual
contests.

| Source | Problem or set | Focus | Status |
|---|---|---|---|
| Codeforces | [1552A. Subsequence Permutation](https://codeforces.com/problemset/problem/1552/A) | quick statement parsing and implementation | required |
| Codeforces | [1185C2. Exam in BerSU (hard version)](https://codeforces.com/problemset/problem/1185/C2) | time pressure and a trusted data structure | required |
| AtCoder | [ABC 141 D. Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d) | heap implementation discipline | required |
| AtCoder | [ABC 131 F. Must Be Rectangular!](https://atcoder.jp/contests/abc131/tasks/abc131_f) | team modeling discussion before coding | optional |
| ICPC/Kattis | [ACM Contest Scoring](https://open.kattis.com/problems/acm) | scoreboard-rule simulation | required |
| ICPC/Kattis | [ICPC Team Selection](https://open.kattis.com/problems/icpcteamselection) | read constraints before choosing a greedy | challenge |

## Four-session training loop

Run these sessions in order with fresh problems. Repeat the loop, increasing
difficulty only after the advancement criteria in the lesson are met.

| Session | Clock | Team setup | Deliverable before the next session |
|---|---:|---|---|
| Solo model sprint | 75 min | individual, no discussion | three pre-code contracts and a read-to-model time for each problem |
| Paired handoff | 90 min | pairs, one keyboard | two-minute handoff notes and one reviewer-created test per problem |
| Team sprint | 120 min | target team and keyboard count | board history, every submission's test label, and classified failures |
| Full virtual | target contest length | target contest rules | 20-minute upsolve attempt per unsolved problem and one next drill per gap |

Use a fixed post-session record, not memory:

```text
problem | owner | model at first attempt | verdict | failure category
counterexample or test | missing observation | next drill
```

The record is useful only when it changes the next session. For example, two
model errors around resource consumption justify a state-expansion drill;
three format errors justify a short parser and output-review drill, not another
unfocused virtual contest.

## Five-hour simulation

Run this with the number of teammates and machines permitted by your target
contest. Use one fixed problem set, no editorials, no internet searching, and
the actual contest's rule sheet.

### Before the clock

1. Build and run every notebook template once on its tiny example.
2. Assign one person to maintain the shared board and one person to monitor
   the clock; roles may rotate.
3. Put three columns on the board: `owner`, `current claim`, and `next test`.
4. Agree on the handoff format: model, invariant, counterexample or blocker,
   and next action.

### First 15 minutes

Each teammate reads every statement shallowly. For every problem, write one
line: likely model, estimated time, and biggest risk. Do not turn that line
into a solution claim yet. Pick the first work only after the entire set has
been scanned.

### During the contest

- A problem has one owner and can have one reviewer; it has no silent second
  implementation.
- Before code reaches the keyboard, the owner states the input model,
  invariant, target complexity, and two edge cases.
- A reviewer independently simulates a sample and one adversarial tiny case.
- After 15 minutes without a concrete model, park the problem and write the
  blocker on the board.
- After a wrong answer, classify it as parsing, model, proof, implementation,
  or test gap before changing code.

### After the clock

For every unsolved problem, spend a fixed 20 minutes trying again before
opening an editorial. Record the missing observation, not just the final
algorithm. Turn repeated mistakes into a test case or a one-line notebook
warning.

## Readiness gate

Repeat full simulations until the team can do all of the following without
slowing down:

- reconstruct every notebook template from its stated invariant;
- hand off an unfinished problem in under two minutes;
- identify the smallest counterexample for a suspected bug;
- upsolve every unsolved problem to a proof and implementation;
- name a concrete corrective action for every wrong submission.
