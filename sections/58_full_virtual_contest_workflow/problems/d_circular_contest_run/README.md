# D. Circular Contest Run

The `n` problems of a training contest are arranged in a circle. Problem `i`
takes `time[i]` minutes. Choose a starting problem and solve consecutive
problems clockwise, using at most `budget` minutes. You may solve each problem
at most once.

Print the maximum number of problems that can be solved.

## Input

```text
n budget
time1 time2 ... timen
```

## Constraints

- `1 <= n <= 200000`
- `1 <= time[i] <= 10^12`
- `0 <= budget <= 10^18`

## Sample

```text
5 8
4 2 1 5 2
```

```text
3
```
