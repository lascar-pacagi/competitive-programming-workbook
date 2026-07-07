# A. Festival Invite

There are `n` villages connected by `n-1` roads, forming a tree. Village `i`
has happiness value `h[i]`. You want to invite some villages to a festival, but
no two adjacent villages may both be invited.

Find the maximum total happiness.

## Input

```text
n
h1 h2 ... hn
u1 v1
...
u(n-1) v(n-1)
```

`1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`.

## Output

Print the maximum total happiness.

## Sample

Input:

```text
5
5 1 4 6 3
1 2
1 3
3 4
3 5
```

Output:

```text
14
```

