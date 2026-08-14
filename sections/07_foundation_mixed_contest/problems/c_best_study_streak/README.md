# C. Best Study Streak

## Statement

You are given an array `a` of `n` nonnegative daily study times: `a[i]` is the
amount of time studied on day `i`. Thus the array positions are consecutive
days `1, 2, 3, ..., n`.

Choose two days `L` and `R` with `L <= R`. The chosen streak consists of every
day from `L` through `R`, so its total study time is
`a[L] + a[L+1] + ... + a[R]`. It is valid when that total is at most the budget
`k`.

Print the maximum length of such a streak and the earliest 1-indexed starting
position among maximum-length streaks. If no nonempty streak is valid, print
`0 0`.

### Example

For `a = [1, 2, 1, 2, 1]` and `k = 4`, read the array as:

```text
day i:            1  2  3  4  5
study time a[i]:  1  2  1  2  1
```

Choosing `L = 1` and `R = 3` means choosing days 1, 2, and 3. Their total is
`a[1] + a[2] + a[3] = 1 + 2 + 1 = 4`, so this is a valid streak of length 3.

Choosing `L = 3` and `R = 5` is another valid streak of length 3. A streak of
four consecutive days is too expensive: days 1 through 4 have total
`1 + 2 + 1 + 2 = 6`, which is greater than `k = 4`. Therefore the answer is:

```text
3 1
```

The `1` is chosen because the streak starting on day 1 is earlier than the
equally long streak starting on day 3. The days in a streak must be consecutive:
you may not skip a day in the middle. For example, choosing days 1, 3, and 5 is
not a streak.

## Input

```text
T
n k
a1 a2 ... an
...
```

`1 <= T <= 50`, the total `n` over all test cases is at most `200000`,
`0 <= ai`, and `0 <= k`.

## Output

For each test case, print:

```text
best_length earliest_start
```
