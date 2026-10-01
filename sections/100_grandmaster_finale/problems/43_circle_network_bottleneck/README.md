# Fibre Network Length

`n` towns are points in the plane. A fibre cable may join any two towns and
costs their Euclidean distance. Print the minimum total cost of cables that
connect all towns.

## Input

```text
n
n lines: x y
```

- `0 <= n <= 2500` (the answer is `0` when `n <= 1`);
- integer coordinates with `|x|, |y| <= 10^9`;
- no three towns are collinear and no four are concyclic.

## Output

Print the minimum total length. Answers with absolute or relative error at most
`10^-7` are accepted.

## Sample input

```text
3
0 0
2 0
0 2
```

## Sample output

```text
4.0000000000
```
