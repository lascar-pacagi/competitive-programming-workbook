# Q. Coprime Rectangles

For each query `(A,B)`, count ordered pairs `(x,y)` such that
`1 <= x <= A`, `1 <= y <= B`, and `gcd(x,y)=1`.

There are at most `5000` queries and `A,B <= 1000000`.

## Input

```text
q
A_1 B_1
...
A_q B_q
```

## Output

Print one answer per query modulo `1000000007`.

## Sample

```text
3
1 5
2 2
3 3
```

```text
5
3
7
```
