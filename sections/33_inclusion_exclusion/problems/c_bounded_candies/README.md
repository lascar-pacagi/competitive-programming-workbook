# C. Bounded Candies

For each query, count the number of ways to distribute `s` identical candies
among `n` distinct children so that every child receives at most `b` candies.

Print each answer modulo `1,000,000,007`.

## Input

```text
q
n1 s1 b1
n2 s2 b2
...
nq sq bq
```

`1 <= q <= 5000`, `1 <= n <= 5000`, `0 <= s <= 5000`, `0 <= b <= 5000`.

Additionally, across all queries,

```text
sum min(n, floor(s / (b + 1))) <= 1,000,000.
```

## Output

Print one answer per query.

## Sample

Input:

```text
4
3 4 2
3 4 4
2 5 2
5 0 0
```

Output:

```text
6
15
0
1
```
