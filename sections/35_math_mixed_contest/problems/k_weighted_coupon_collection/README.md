# K. Weighted Coupon Collection

There are `n` coupon types. On each independent draw, coupon `i` appears with
probability `weight[i] / W`, where `W` is the sum of all weights.

Find the expected number of draws until every coupon type has appeared at
least once. Print the expectation modulo `1000000007`: a fraction `p/q` is
represented as `p * q^(-1)` modulo that prime.

## Input

```text
n
weight[1] weight[2] ... weight[n]
```

`1 <= n <= 20`, every weight is positive, and
`sum(weight) < 1000000007`.

## Output

Print the modular expectation.

## Sample

```text
2
1 1
```

```text
3
```
