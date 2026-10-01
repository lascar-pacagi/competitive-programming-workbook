# Lantern Grid

A festival hangs lanterns in an `n x m` grid; each lantern is on (`1`) or off
(`0`). Pressing the button of a lantern toggles that lantern and its up to
four side neighbours. Every button may be pressed at most once, and the order
of presses does not matter.

Count the sets of buttons whose pressing turns every lantern off, modulo
`1,000,000,007`.

## Input

```text
n m
n lines: a string of m characters 0/1
```

- `1 <= n, m <= 1000`.

## Output

Print the number of press sets modulo `1,000,000,007`.

## Sample input

```text
3 3
010
111
010
```

## Sample output

```text
1
```

Pressing only the centre button works, and it is the only way.
