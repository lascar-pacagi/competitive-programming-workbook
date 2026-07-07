# A. Expected Prize

There are `n` independent bonus events. Event `i` happens with probability
`p[i] / q[i]`. If it happens, you gain `v[i]` points; otherwise you gain `0`
points from that event.

Print the expected total number of points modulo `1,000,000,007`.

## Input

```text
n
p1 q1 v1
p2 q2 v2
...
pn qn vn
```

`1 <= n <= 200,000`, `0 <= p[i] <= q[i]`, `1 <= q[i] < MOD`,
`0 <= v[i] <= 10^9`.

## Output

Print the expected value modulo `1,000,000,007`.

## Sample

Input:

```text
3
1 2 10
1 4 8
3 4 12
```

Output:

```text
16
```
