# B. Ticket Split

## Statement

You need to buy exactly `n` tickets for exactly `s` coins.

There are three ticket types:

- type A costs `a` coins;
- type B costs `b` coins;
- type C costs `c` coins.

For each test case, determine whether there exist nonnegative integers
`x`, `y`, and `z` such that:

```text
x + y + z = n
a*x + b*y + c*z = s
```

If a solution exists, print the first valid triple found by checking `x` from
`0` to `n`, and for each `x`, checking `y` from `0` to `n - x`. Otherwise
print `-1`.

## Input

```text
T
n s a b c
...
```

`1 <= T <= 100`, `0 <= n <= 300`, and all costs and sums are between `0` and
`100000`.

## Output

For each test case, print the required first valid triple or `-1`.
