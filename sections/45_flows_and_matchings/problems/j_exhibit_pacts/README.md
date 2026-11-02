# J. Exhibit Pacts

A museum chooses which of `n` exhibits to open. Opening exhibit `i` contributes
signed value `w[i]`; leaving it closed contributes zero. Negative values
represent operating expenses.

Sponsors offer `g` independent pacts. A pact names a nonempty group of exhibits
and a nonnegative bonus:

- Type 1 pays its bonus if **all** exhibits in its group are open.
- Type 0 pays its bonus if **all** exhibits in its group are closed.

A pact that is not satisfied pays zero; it does not forbid the configuration.
Groups may overlap, and every satisfied pact pays its full bonus independently.
Choose the open exhibits to maximize the sum of their signed values and all
paid bonuses. Opening no exhibit is allowed.

## Input

```text
n g
w1 ... wn
type1 bonus1 size1 member1 ... member_size1
...
typeg bonusg sizeg member1 ... member_sizeg
```

- `1 <= n <= 120`, `0 <= g <= 200`.
- `-10^9 <= wi <= 10^9`, `0 <= bonusk <= 10^9`.
- `typek` is 0 or 1; `1 <= sizek <= n`.
- IDs within a group are distinct and in `[1,n]`.
- The sum of all group sizes is at most 3000. Different pacts may name the
  same group, even with different types.

## Output

Print the maximum total value as a signed 64-bit integer.

## Sample

```text
3 2
4 -5 2
1 6 2 1 2
0 5 2 2 3
```

```text
9
```

Open only exhibit 1. Its value is four and the second pact pays five.
Opening all three would pay the first pact but give total value only seven.
