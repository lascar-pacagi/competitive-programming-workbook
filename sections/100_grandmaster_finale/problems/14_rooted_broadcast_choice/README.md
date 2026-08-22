# Rooted Broadcast Choice

There are `n` stations. Activating station `r` as the unique broadcaster costs
`a[r]`. A directed link `u -> v` costs `c` and allows station `v` to receive a
message after `u` has received it.

Choose one broadcaster and exactly `n-1` directed links so that every station
is reachable from the broadcaster. Minimize the activation cost plus the link
costs. Print `-1` if this is impossible.

Parallel directed links are allowed.

## Input

```text
n m
a[1] ... a[n]
m lines: u v c
```

- `1 <= n <= 200`;
- `0 <= m <= 5000`;
- `1 <= a[i], c <= 10^9`;
- `u != v`.

## Output

Print the minimum total cost, or `-1`.

## Sample input

```text
4 5
10 3 8 20
1 2 2
2 3 2
3 4 2
4 1 1
2 1 7
```

## Sample output

```text
8
```
