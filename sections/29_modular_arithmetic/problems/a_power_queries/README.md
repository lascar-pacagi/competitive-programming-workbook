# A. Power Queries

You are given `q` independent queries. For each query, compute:

```text
a^b mod m
```

## Input

```text
q
a1 b1 m1
a2 b2 m2
...
aq bq mq
```

`1 <= q <= 2 * 10^5`, `0 <= a <= 10^18`, `0 <= b <= 10^18`,
`1 <= m <= 10^9 + 7`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
2 10 1000
5 0 7
10 3 6
123456789 2 1000000007
```

Output:

```text
24
1
4
643499475
```
