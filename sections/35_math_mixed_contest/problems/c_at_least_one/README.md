# C. At Least One

There are `n` independent events. Event `i` happens with probability `p[i]/q[i]`.

Print the probability that at least one event happens, modulo `1,000,000,007`.

## Input

```text
n
p1 q1
p2 q2
...
pn qn
```

`1 <= n <= 200,000`, `0 <= p[i] <= q[i]`, `1 <= q[i] < MOD`.

## Output

Print the probability modulo `1,000,000,007`.

## Sample

Input:

```text
2
1 2
1 3
```

Output:

```text
666666672
```
