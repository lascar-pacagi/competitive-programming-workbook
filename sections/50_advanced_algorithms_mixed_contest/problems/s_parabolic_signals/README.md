# S. Parabolic Signals

There are `n` transmitters on a line. Transmitter `i` has position `p[i]`
and signed base strength `b[i]`. At coordinate `x`, its received strength is

```text
b[i] - (x - p[i])^2
```

For each of `q` receiver coordinates, print the strongest received strength
among all transmitters. All transmitters are available for every query; they
are not consumed. Strengths may be negative, and a receiver must still report
the largest one rather than replacing it with zero.

## Input

The first line contains `n q`. Each of the next `n` lines contains `p[i] b[i]`.
The final line contains the `q` receiver coordinates, in query order.

- `1 <= n, q <= 200000`.
- `-1000000 <= p[i], x <= 1000000`.
- `-1000000000000 <= b[i] <= 1000000000000`.
- Positions and receiver coordinates need not be sorted and may repeat.

## Output

Print one maximum strength per line, in query order. Use signed 64-bit
arithmetic for the squared distances and results.

## Sample

Input:

```text
2 3
0 5
4 8
0 2 5
```

Output:

```text
5
4
7
```

At coordinate `2`, the strengths are `1` and `4`; at coordinate `5`, they
are `-20` and `7`.
