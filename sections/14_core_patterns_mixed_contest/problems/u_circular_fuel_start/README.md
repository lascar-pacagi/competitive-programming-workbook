# U. Circular Fuel Start

There are `n` stations on a directed circle. At station `i`, you receive
`fuel_i` units of fuel. Travelling from station `i` to station `(i+1) mod n`
costs `cost_i` units. The tank starts empty and has unlimited capacity.

Print the smallest zero-based station index from which you can complete one
full circuit without the fuel level ever becoming negative, or `-1` if no such
start exists.

## Input

```text
n
fuel0 fuel1 ... fuel(n-1)
cost0 cost1 ... cost(n-1)
```

`1 <= n <= 200000` and `0 <= fuel_i, cost_i <= 10^9`.

## Output

Print the smallest valid zero-based starting index, or `-1`.

## Sample Input

```text
5
1 2 3 4 5
3 4 5 1 2
```

## Sample Output

```text
3
```
