# I. Grouped Cargo

Cargo items are divided into `g` groups. Item `j` in a group has a weight and
a value. Choose at most one item from each group, with total weight at most
`W`, and maximize the total value.

## Input

The first line contains `g` and `W`.

Each group is then described on one line:

```text
c w1 v1 w2 v2 ... wc vc
```

where `c` is the number of items in that group.

`1 <= g <= 200`

`1 <= W <= 5000`

The total number of items over all groups is at most `2000`.

`1 <= weight <= W`, `0 <= value <= 10^9`.

## Output

Print the maximum total value.

## Sample Input

```text
3 7
2 3 5 4 8
2 2 4 5 10
1 3 7
```

## Sample Output

```text
15
```
