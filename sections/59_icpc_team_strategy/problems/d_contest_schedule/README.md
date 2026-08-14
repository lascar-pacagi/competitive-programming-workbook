# D. Contest Schedule

You have `n` problems and `limit` minutes of contest time. Solving problem `i`
takes `time[i]` minutes. You work on one problem at a time.

Choose an order that maximizes the number of solved problems. Among all such
orders, minimize total penalty, defined as the sum of completion times of the
solved problems.

## Input

```text
n limit
time1 time2 ... timen
```

## Constraints

```text
1 <= n <= 200,000
1 <= limit, time[i] <= 1,000,000,000,000
```

## Output

Print two integers:

```text
maximum_solved minimum_penalty
```

## Sample

Input:

```text
4 5
3 1 2 2
```

Output:

```text
3 9
```
