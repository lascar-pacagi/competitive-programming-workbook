# B. Range Add Final Array

## Statement

You start with an array of `n` zeros. Then you receive `q` range-add updates.
Each update gives 1-indexed inclusive endpoints `l`, `r`, and a value `x`.
Add `x` to every position from `l` through `r`.

After all updates, print the final array.

## Input

```text
T
n q
l1 r1 x1
...
lq rq xq
...
```

`1 <= T <= 30`, the total `n + q` over all test cases is at most `200000`, and
all update values fit in signed 32-bit integers.

## Output

For each test case, print the final array on one line.

