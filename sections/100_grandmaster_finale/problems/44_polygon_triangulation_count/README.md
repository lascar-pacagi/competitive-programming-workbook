# Polygon Triangulation Count

A plot of land is a simple polygon (its boundary does not cross itself) with
`n` corners given in order around the boundary, either clockwise or
counterclockwise. No three corners are collinear.

A **triangulation** cuts the plot into `n - 2` triangles using `n - 3`
straight cuts between corners; every cut must run through the interior of the
plot, and no two cuts may cross. Count the triangulations modulo
`1,000,000,007`.

## Input

```text
n
n lines: x y
```

- `3 <= n <= 300`;
- `|x|, |y| <= 10^9`;
- the polygon is simple and no three corners are collinear.

## Output

Print the number of triangulations modulo `1,000,000,007`.

## Sample input

```text
6
0 0
4 0
4 4
2 1
0 4
-1 2
```

## Sample output

```text
3
```
