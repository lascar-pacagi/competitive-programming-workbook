# Fleet Pairing

A delivery company owns `n` drones. Some pairs of drones can be flown as a
tandem; offer `i` says that drones `u[i]` and `v[i]` flying together earn a
profit of `w[i]`. Several offers may name the same pair (only one of them can
be used), and an offer naming the same drone twice is invalid and must be
ignored.

Every drone belongs to at most one tandem, and drones may stay alone. Choose
tandems to maximize the total profit, and print that maximum.

## Input

```text
n m
m lines: u v w
```

- `1 <= n <= 500`, `0 <= m <= 50000`;
- `1 <= u, v <= n`;
- `1 <= w <= 10^6`.

## Output

Print the maximum total profit.

## Sample input

```text
6 8
1 2 5
2 3 6
3 1 5
3 4 4
4 5 3
5 6 5
6 4 3
1 2 7
```

## Sample output

```text
16
```

Tandems `(1,2)` with the second offer, `(3,4)` and `(5,6)` earn `7 + 4 + 5`.
