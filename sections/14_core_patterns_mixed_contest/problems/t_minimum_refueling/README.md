# T. Minimum Refueling

A vehicle starts at position `0` with enough fuel to travel `F` distance units.
Its destination is at position `D`. Station `i` is at position `position_i` and
provides exactly `fuel_i` additional distance units if you stop there. Fuel can
be accumulated, and stopping does not consume distance or time.

Print the minimum number of stations at which the vehicle must stop to reach
the destination, or `-1` if it is impossible.

## Input

```text
D F n
position1 fuel1
position2 fuel2
...
positionn fueln
```

`1 <= D <= 10^18`, `0 <= F <= 10^18`, `0 <= n <= 200000`, and
`1 <= position_i < D`, `1 <= fuel_i <= 10^18`. Station positions are distinct
but are not necessarily given in sorted order.

## Output

Print the minimum number of refueling stops, or `-1`.

## Sample Input

```text
100 10 4
10 60
20 30
30 30
60 40
```

## Sample Output

```text
2
```
