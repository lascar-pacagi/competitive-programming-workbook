# A. Network Growth

There are `n` computers and initially no cables. Cables are added one by one.
After each added cable, print:

1. the current number of connected components;
2. the size of the largest connected component.

## Input

```text
n m
u1 v1
u2 v2
...
um vm
```

`1 <= n <= 2 * 10^5`  
`1 <= m <= 2 * 10^5`

Computers are numbered from `1` to `n`. Repeated cables may appear.

## Output

Print `m` lines. After the `i`-th cable, print:

```text
components largest
```

## Sample

Input:

```text
5 4
1 2
3 4
2 3
2 4
```

Output:

```text
4 2
3 2
2 4
2 4
```

