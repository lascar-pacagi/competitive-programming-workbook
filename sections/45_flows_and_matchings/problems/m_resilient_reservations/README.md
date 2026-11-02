# M. Resilient Reservations

Every one of `n` visitors needs a different appointment slot. There are `m`
slots, and each visitor accepts a listed subset. Before appointments are
assigned, an adversary may cancel some slots. After seeing the cancellations,
you may choose a completely new assignment using the remaining slots.

Find the largest integer `k` such that **every** cancellation of at most `k`
slots still permits all visitors to receive distinct accepted slots.
The guarantee must hold against any choice of cancelled slots, not only
against a random choice or for one fixed assignment.

## Input

```text
n m e
visitor1 slot1
...
visitore slote
```

- `1 <= n <= 60`, `1 <= m <= 200`, `0 <= e <= n*m`.
- Each listed pair has visitor ID in `[1,n]` and slot ID in `[1,m]`.
- No pair is listed twice. Slots accepted by nobody may still be cancelled.

## Output

Print the largest valid `k` in `[0,m]`. Print `-1` if a complete assignment
is impossible even when no slot is cancelled.

## Sample

```text
2 4 5
1 1
1 2
2 2
2 3
2 4
```

```text
1
```

After any one cancellation both visitors can still be accommodated. However,
cancelling slots 1 and 2 leaves visitor 1 with no acceptable slot. Thus merely
having two more slots than visitors does not guarantee tolerance of two losses.
