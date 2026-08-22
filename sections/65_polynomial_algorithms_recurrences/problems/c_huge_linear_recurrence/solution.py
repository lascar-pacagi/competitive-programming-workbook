import sys

MOD = 998_244_353


def combine(left: list[int], right: list[int], coefficient: list[int]) -> list[int]:
    order = len(coefficient)
    product = [0] * (2 * order - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % MOD
    for degree in range(2 * order - 2, order - 1, -1):
        value = product[degree]
        for back, coefficient_value in enumerate(coefficient, 1):
            product[degree - back] = (
                product[degree - back] + value * coefficient_value
            ) % MOD
    return product[:order]


def nth_term(initial: list[int], coefficient: list[int], index: int) -> int:
    order = len(initial)
    if index < order:
        return initial[index]
    result = [1] + [0] * (order - 1)
    base = [coefficient[0]] if order == 1 else [0, 1] + [0] * (order - 2)
    while index:
        if index & 1:
            result = combine(result, base, coefficient)
        base = combine(base, base, coefficient)
        index >>= 1
    return sum(a * b for a, b in zip(result, initial)) % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    order, index = data[:2]
    initial = data[2 : 2 + order]
    coefficient = data[2 + order : 2 + 2 * order]
    print(nth_term(initial, coefficient, index))


if __name__ == "__main__":
    main()
