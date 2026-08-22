# B. Bounded Sum Product

There are `n` independent dials. Dial `i` may be set to any integer from `0`
through `ai`, inclusive. Count the settings whose total is exactly `K`, modulo
`998244353`.

## Input

```text
n K
a1 a2 ... an
```

- `1 <= n <= 5000`
- `0 <= K <= 50000`
- `0 <= ai <= K`
- the sum of `min(ai+1, K+1)` over all dials is at most `200000`

## Output

Print the required count modulo `998244353`.

## Sample

```text
3 4
1 2 3
```

```text
5
```
