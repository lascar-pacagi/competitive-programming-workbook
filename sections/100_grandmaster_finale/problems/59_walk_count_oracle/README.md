# Walk Count Oracle

A transit map has `n` stops and `m` numbered one-way tracks. Track `i` goes
from stop `u[i]` to stop `v[i]`; loops and repeated tracks are allowed and
count as different tracks.

A journey of length `N` is a sequence of `N` tracks where each track starts
at the stop where the previous one ended. Journeys are different when their
track sequences differ. A journey of length `0` stays at its starting stop.

Count the journeys of length exactly `N` that start at stop `s` and end at
stop `t`, modulo `998244353`.

## Input

```text
n m N s t
m lines: u v
```

- `1 <= n <= 1000`, `0 <= m <= 10000`;
- `0 <= N <= 10^18`;
- `1 <= s, t, u, v <= n`.

## Output

Print the number of journeys modulo `998244353`.

## Sample input

```text
3 5 4 1 3
1 2
2 3
3 1
2 1
1 1
```

## Sample output

```text
2
```

The journeys are `1 -> 1 -> 1 -> 2 -> 3` and `1 -> 2 -> 1 -> 2 -> 3`.
