import sys

MOD = 998_244_353


def berlekamp_massey(sequence: list[int]) -> list[int]:
    current, saved = [1], [1]
    length, shift, saved_discrepancy = 0, 1, 1
    for position, term in enumerate(sequence):
        discrepancy = term
        for i in range(1, length + 1):
            discrepancy = (discrepancy + current[i] * sequence[position - i]) % MOD
        if discrepancy == 0:
            shift += 1
            continue
        previous = current[:]
        scale = discrepancy * pow(saved_discrepancy, MOD - 2, MOD) % MOD
        current += [0] * max(0, len(saved) + shift - len(current))
        for i, value in enumerate(saved):
            current[i + shift] = (current[i + shift] - scale * value) % MOD
        if 2 * length <= position:
            length = position + 1 - length
            saved = previous
            saved_discrepancy = discrepancy
            shift = 1
        else:
            shift += 1
    return [(-current[i]) % MOD for i in range(1, length + 1)]


def combine(left: list[int], right: list[int], recurrence: list[int]) -> list[int]:
    order = len(recurrence)
    product = [0] * (2 * order - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % MOD
    for degree in range(2 * order - 2, order - 1, -1):
        value = product[degree]
        for back, coefficient in enumerate(recurrence, 1):
            product[degree - back] = (
                product[degree - back] + value * coefficient
            ) % MOD
    return product[:order]


def nth_term(sequence: list[int], recurrence: list[int], index: int) -> int:
    if index < len(sequence):
        return sequence[index]
    order = len(recurrence)
    if order == 0:
        return 0
    result = [1] + [0] * (order - 1)
    base = [recurrence[0]] if order == 1 else [0, 1] + [0] * (order - 2)
    while index:
        if index & 1:
            result = combine(result, base, recurrence)
        base = combine(base, base, recurrence)
        index >>= 1
    return sum(result[i] * sequence[i] for i in range(order)) % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, walk_length, start, target = data[:5]
    start -= 1
    target -= 1
    edges = []
    index = 5
    for _ in range(m):
        u, v, weight = data[index : index + 3]
        index += 3
        edges.append((u - 1, v - 1, weight))
    state = [0] * n
    state[start] = 1
    sequence = []
    for _ in range(2 * n + 1):
        sequence.append(state[target])
        next_state = [0] * n
        for u, v, weight in edges:
            next_state[v] = (next_state[v] + state[u] * weight) % MOD
        state = next_state
    recurrence = berlekamp_massey(sequence)
    print(nth_term(sequence, recurrence, walk_length))


if __name__ == "__main__":
    main()
