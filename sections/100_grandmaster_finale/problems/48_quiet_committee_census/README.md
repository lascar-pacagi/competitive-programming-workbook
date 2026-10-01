# Quiet Committee Census

A club has `n` members; member `i` has prestige `w[i]`. Some pairs of members
are rivals. A committee is any set of members (possibly empty) that contains
no two rivals, and its prestige is the sum of its members' prestige.

Print the maximum possible prestige of a committee and the number of
committees attaining it, modulo `1,000,000,007`.

## Input

```text
n m
w[1] ... w[n]
m lines: u v      (u and v are rivals)
```

- `1 <= n <= 40`;
- `0 <= m <= n(n-1)/2`, and pairs may repeat;
- `0 <= w[i] <= 10^9`.

## Output

Print `best count`.

## Sample input

```text
5 5
3 2 2 1 4
1 2
2 3
3 4
4 5
5 1
```

## Sample output

```text
6 2
```

The best committees are `{2, 5}` and `{3, 5}`.
