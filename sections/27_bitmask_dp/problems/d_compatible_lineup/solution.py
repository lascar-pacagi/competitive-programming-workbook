import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    score = [next(it) for _ in range(n)]
    incompatible = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        incompatible[u] |= 1 << v
        incompatible[v] |= 1 << u

    total_masks = 1 << n
    total = [0] * total_masks
    compatible = bytearray(total_masks)
    compatible[0] = 1
    answer = 0

    for mask in range(1, total_masks):
        lowest_bit = mask & -mask
        performer = lowest_bit.bit_length() - 1
        previous = mask ^ lowest_bit
        total[mask] = total[previous] + score[performer]
        if compatible[previous] and not (incompatible[performer] & previous):
            compatible[mask] = 1
            if total[mask] > answer:
                answer = total[mask]

    print(answer)


if __name__ == "__main__":
    main()
