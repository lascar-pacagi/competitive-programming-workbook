# C. Energy Route

There are `n` platforms in a line. Platform `i` has height `h[i]`. You start on
platform `1` and want to reach platform `n`.

From platform `i`, you may jump to any platform `j` with `i < j <= i + k`.
The energy cost of that jump is `abs(h[i] - h[j])`.

Find the minimum total energy needed to reach platform `n`.

## Input

```text
n k
h1 h2 ... hn
```

`1 <= n <= 2 * 10^5`, `1 <= k <= 50`, `0 <= hi <= 10^9`.

## Output

Print the minimum total energy.

## Sample

Input:

```text
5 3
10 30 40 50 20
```

Output:

```text
30
```

