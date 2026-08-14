# K. Last Crystal Removed

`n` crystals stand in a row, with positive values `a[1], ..., a[n]`. Two
permanent boundary crystals of value `1` stand immediately outside the row.

When you remove a remaining crystal with value `x`, let `L` and `R` be the
nearest crystals still present to its left and right, including the permanent
boundary crystals. You gain:

```text
value[L] * x * value[R]
```

Remove all original crystals and maximize the total gain.

## Input

```text
n
a[1] a[2] ... a[n]
```

`1 <= n <= 300`

`1 <= a[i] <= 1000`

The answer fits in a signed 64-bit integer.

## Output

Print the maximum total gain.

## Sample Input

```text
4
3 1 5 8
```

## Sample Output

```text
167
```
