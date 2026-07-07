"""Reference solution for C. Token Budget."""

import sys


def ceil_log2_for_estimate(n: int) -> int:
    return max(1, (n - 1).bit_length())


def classify(n: int, budget: int) -> str:
    log = ceil_log2_for_estimate(n)
    estimates = [
        ("cubic", n * n * n),
        ("quadratic", n * n),
        ("nlogn", n * log),
        ("linear", n),
    ]
    for label, cost in estimates:
        if cost <= budget:
            return label
    return "none"


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    out: list[str] = []
    idx = 1
    for _ in range(q):
        n = data[idx]
        budget = data[idx + 1]
        idx += 2
        out.append(classify(n, budget))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

