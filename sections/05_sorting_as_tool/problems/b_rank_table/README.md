# B. Rank Table

## Statement

For each test case, you are given contestants with:

- a name;
- a score;
- a penalty.

Sort the contestants by:

1. higher score first;
2. if scores tie, lower penalty first;
3. if both tie, lexicographically smaller name first.

Print the names in sorted order.

## Input

```text
T
n
name1 score1 penalty1
...
namen scoren penaltyn
...
```

Names contain only lowercase English letters. `1 <= T <= 30`, the total `n`
over all test cases is at most `200000`.

## Output

For each test case, print the sorted names on one line.

