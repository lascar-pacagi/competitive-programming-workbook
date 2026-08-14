# A. Skill Coverage

There are `n` required skills, numbered from `1` to `n`, and `m` available
candidates. Candidate `i` has cost `c[i]` and knows some subset of the skills.

Choose any number of candidates with minimum total cost so that every required
skill is covered by at least one chosen candidate.

If it is impossible to cover all skills, print `-1`.

## Input

The first line contains:

```text
n m
```

- `n` is the number of required skills;
- `m` is the number of candidates.

The next `m` lines describe one candidate each. Candidate `i` is written as:

```text
c[i] k[i] skill[1] skill[2] ... skill[k[i]]
```

- `c[i]` is the cost of choosing this candidate;
- `k[i]` is the number of skills this candidate knows;
- exactly `k[i]` skill numbers follow on the same line.

For example:

```text
5 2 1 2
```

means that the candidate costs `5` and knows `2` skills: skills `1` and `2`.

Constraints:

```text
1 <= n <= 20
1 <= m <= 30
1 <= c[i] <= 10^9
1 <= k[i] <= n
1 <= skill[j] <= n
```

The skill numbers listed for one candidate are distinct.

## Output

Print the minimum possible cost, or `-1`.

## Sample

Input:

```text
4 5
5 2 1 2
6 2 2 3
4 1 4
7 3 1 3 4
3 1 2
```

The five candidate lines mean:

| Candidate | Cost | Number of skills | Skills known |
|---:|---:|---:|---|
| 1 | 5 | 2 | 1, 2 |
| 2 | 6 | 2 | 2, 3 |
| 3 | 4 | 1 | 4 |
| 4 | 7 | 3 | 1, 3, 4 |
| 5 | 3 | 1 | 2 |

Output:

```text
10
```
