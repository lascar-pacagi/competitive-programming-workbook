# Chronicle Path Dictionary

An old kingdom is a tree of `n` towns. Town `v` keeps a chronicle marked with
one lowercase letter `c[v]`. Travelling along the unique simple path from town
`u` to town `v` and reading the letters in order (both ends included) gives
the string `S(u,v)`. Note that `S(v,u)` is `S(u,v)` reversed.

For each query `(u, v, p)`, print how many times the word `p` occurs in
`S(u,v)` as a contiguous substring. Occurrences may overlap.

## Input

```text
n q
c[1] c[2] ... c[n]      (one string of length n)
n-1 lines: a b          (tree edges)
q lines: u v p
```

- `1 <= n, q <= 100000`;
- `p` is a nonempty lowercase word, and the total length of all words is at
  most `200000`.

## Output

Print one line per query.

## Sample input

```text
7 4
abaabba
1 2
1 3
2 4
2 5
3 6
6 7
4 7 ab
7 4 ab
5 6 aba
4 4 a
```

## Sample output

```text
2
2
0
1
```
