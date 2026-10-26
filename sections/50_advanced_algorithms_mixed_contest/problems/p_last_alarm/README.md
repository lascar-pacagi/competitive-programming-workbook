# P. Last Alarm

A network of `n` stations forms a tree. Station `v` emits its alarm at time
`a[v]`. An alarm then travels along tree edges; traversing an edge takes its
specified delay. Signals propagate independently in both directions, without
queues, congestion, or additional processing time.

For each possible receiving station `r`, determine the time when all alarms
have reached it. Its own alarm is received at time `a[r]`. Thus the required
time is the latest arrival among all `n` alarms.

## Input

The first line contains `n`. The second line contains `n` integers
`a[1] ... a[n]`. Each of the next `n-1` lines contains `u v delay`, describing
an undirected edge.

- `1 <= n <= 200000`.
- `0 <= a[v] <= 1000000000`.
- `1 <= u, v <= n`, `u != v`, and `1 <= delay <= 1000000000`.
- The edges form a connected tree.

## Output

Print `n` integers in vertex order: the last arrival time for each receiver.
Values may exceed 32-bit integer range.

## Sample

Input:

```text
3
0 10 0
1 2 2
2 3 3
```

Output:

```text
12 10 13
```

The three arrival times at station `1` are `0`, `12`, and `5`, so its answer
is `12`. At station `2` they are `2`, `10`, and `3`; at station `3`, they are
`5`, `13`, and `0`.
