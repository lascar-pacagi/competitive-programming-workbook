# G. Capped Allocation

Distribute exactly `S` identical tokens among `n` labeled boxes. Box `i` must
receive an integer `x[i]` satisfying `0 <= x[i] <= cap[i]`.

Count the valid distributions modulo `1000000007`.

## Input

```text
n S
cap[1] cap[2] ... cap[n]
```

`1 <= n <= 20`, `0 <= S,cap[i] <= 999999900`.

## Output

Print the number of valid distributions modulo `1000000007`.

## Sample

```text
3 5
2 3 4
```

```text
11
```
