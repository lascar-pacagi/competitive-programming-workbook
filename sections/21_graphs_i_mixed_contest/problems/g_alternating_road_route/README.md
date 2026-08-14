# G. Alternating Road Route

Every directed road has a nonnegative cost and a color, `R` or `B`. Find
the minimum cost from vertex `1` to vertex `n` subject to consecutive roads
having different colors. The first road may have either color.

## Input

```text
n m
u v cost color
...
```

`1 <= n,m <= 200000`.

## Output

Print the minimum cost, or `-1`.

## Sample

```text
4 5
1 2 3 R
2 4 4 B
1 3 1 B
3 4 2 B
3 2 1 R
```

```text
6
```
