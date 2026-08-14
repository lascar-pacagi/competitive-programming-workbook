# Offline companion: ACM Contest Scoring

This is an original, locally judgeable companion for [ACM Contest Scoring](https://open.kattis.com/problems/acm). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


Replay an ICPC-style scoreboard.

## Input

The first line contains `T P S`: the number of teams, problems, and
submissions. Teams and problems are numbered from 1. Each of the next `S`
lines contains `minute team problem verdict`, where `verdict` is `W` (wrong)
or `A` (accepted). Records are in chronological order.

For each team/problem pair, only submissions before the first `A` matter. A
first `A` solves that problem and adds
`minute + 20 * (earlier wrong submissions for that pair)` to the team's
penalty. A wrong submission to a problem that is never accepted adds no
penalty.

## Output

Print every team as `team solved penalty`, ordered by more solved, then lower
penalty, then lower team id.

## Constraints

`1 <= T, P <= 200`, `0 <= S <= 100000`, and minutes fit in a signed 32-bit
integer. The total penalty may not, so use a 64-bit integer.

## Sample

Input:

```text
3 3 9
10 1 1 W
15 2 1 A
20 1 1 W
30 1 1 A
35 2 1 W
40 2 2 W
50 2 2 A
50 3 3 A
60 1 2 W
```

Output:

```text
2 2 85
3 1 50
1 1 70
```
