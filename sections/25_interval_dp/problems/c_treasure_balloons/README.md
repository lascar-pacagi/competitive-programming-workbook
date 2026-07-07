# C. Treasure Balloons

There are `n` balloons in a row. Balloon `i` has value `a[i]`. You will pop all
balloons one by one.

When you pop balloon `i`, your score is:

```text
left_value * a[i] * right_value
```

where `left_value` and `right_value` are the values of the nearest unpopped
balloons immediately to the left and right. If there is no such balloon on a
side, use value `1` for that side.

Find the maximum total score.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200`, `1 <= ai <= 1000`.

## Output

Print the maximum total score.

## Sample

Input:

```text
4
3 1 5 8
```

Output:

```text
167
```

