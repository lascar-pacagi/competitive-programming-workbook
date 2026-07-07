# C. Linear Diophantine

For each query, given positive integers `a`, `b`, and `c`, find any integers
`x` and `y` such that:

```text
a*x + b*y = c
```

If no such integers exist, print `IMPOSSIBLE`.

## Input

```text
q
a1 b1 c1
a2 b2 c2
...
aq bq cq
```

`1 <= q <= 2 * 10^5`, `1 <= a,b,c <= 10^9`.

## Output

For each query, print either:

```text
x y
```

or:

```text
IMPOSSIBLE
```

## Sample

Input:

```text
4
6 10 14
6 10 15
7 5 1
12 18 6
```

Output:

```text
14 -7
IMPOSSIBLE
-2 3
-1 1
```
