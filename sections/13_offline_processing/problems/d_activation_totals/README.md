# D. Activation Totals

Each item has an activation level `a` and a weight `w`. For every query limit
`x`, output the total weight of all items with `a <= x`. Queries must be
answered in input order.

## Input
```text
n q
a1 w1
...
an wn
x1 x2 ... xq
```
`1 <= n,q <= 200000`, and all levels/weights/limits fit in signed 32-bit
integers. Weights may be negative.

## Output
Print q totals on one line in query order.

## Sample
```text
4 4
5 10
1 -3
3 7
5 2
0 1 4 5
```
```text
0 -3 4 16
```
