# D. Penalty Order

All `n` remaining problems will be solved by one team member using one keyboard.
Problem `i` takes exactly `t[i]` minutes once work begins. The penalty charged
for a problem is the minute at which it is completed.

Choose the solving order that minimizes the total penalty of all problems.

## Input

```text
n
t1 t2 ... tn
```

## Constraints

```text
1 <= n <= 200000
1 <= ti <= 1000000000
```

## Output

Print the minimum possible total penalty.

## Sample

```text
4
3 1 2 4
```

```text
20
```

Solving in durations `1,2,3,4` finishes at minutes `1,3,6,10`, whose sum is
`20`.
