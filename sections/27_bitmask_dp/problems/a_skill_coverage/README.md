# A. Skill Coverage

There are `n` required skills, numbered from `1` to `n`, and `m` available
candidates. Candidate `i` has cost `c[i]` and knows some subset of the skills.

Choose any number of candidates with minimum total cost so that every required
skill is covered by at least one chosen candidate.

If it is impossible to cover all skills, print `-1`.

## Input

```text
n m
c1 k1 s1,1 s1,2 ... s1,k1
c2 k2 s2,1 s2,2 ... s2,k2
...
cm km sm,1 sm,2 ... sm,km
```

`1 <= n <= 20`, `1 <= m <= 30`, `1 <= c[i] <= 10^9`.

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

Output:

```text
10
```
