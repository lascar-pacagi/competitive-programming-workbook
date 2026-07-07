# B. First Success

For each query, you repeatedly perform an experiment until it succeeds. Each
attempt succeeds independently with probability `p / q`.

Print the expected number of attempts modulo `1,000,000,007`.

## Input

```text
t
p1 q1
p2 q2
...
pt qt
```

`1 <= t <= 200,000`, `1 <= p <= q < MOD`.

## Output

Print one answer per query.

## Sample

Input:

```text
3
1 2
2 5
7 7
```

Output:

```text
2
500000006
1
```
