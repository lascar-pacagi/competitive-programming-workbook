import argparse
import random
from pathlib import Path


def brute(times, budget):
    answer = 0
    n = len(times)
    for start in range(n):
        total = 0
        for length in range(1, n + 1):
            total += times[(start + length - 1) % n]
            if total <= budget:
                answer = max(answer, length)
    return answer


def small_case(rng):
    n = rng.randint(1, 25)
    budget = rng.randint(0, 100)
    times = [rng.randint(1, 25) for _ in range(n)]
    case = f"{n} {budget}\n" + " ".join(map(str, times)) + "\n"
    return case, f"{brute(times, budget)}\n"


def scale_case():
    n = 200_000
    budget = 100_000
    case = f"{n} {budget}\n" + "1 " * (n - 1) + "1\n"
    return case, f"{budget}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = (
            scale_case() if case_id == 0 else small_case(rng)
        )
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
