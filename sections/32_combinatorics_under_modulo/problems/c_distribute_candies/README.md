# C. Distribute Candies

For each query, count the number of ways to distribute `s` identical candies
among `n` distinct children. Children may receive zero candies.

Print each answer modulo `1,000,000,007`.

## Input

```text
q
n1 s1
n2 s2
...
nq sq
```

`1 <= q <= 200,000`, `1 <= n <= 1,000,000`, `0 <= s <= 1,000,000`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
3 4
1 10
5 0
2 3
```

Output:

```text
15
1
1
4
```
