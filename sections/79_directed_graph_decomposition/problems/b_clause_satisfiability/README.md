# Clause Satisfiability

There are `n` Boolean variables and `m` clauses. A literal is a signed integer: `x` means variable `x` is true and `-x` means it is false. Decide whether all clauses `(a OR b)` can hold simultaneously.

Input: `n m`, then the two literals of each clause; `n,m <= 200000`.

Output: `YES` or `NO`.

Sample input
```text
2 3
1 2
-1 2
-2 1
```
Sample output
```text
YES
```
