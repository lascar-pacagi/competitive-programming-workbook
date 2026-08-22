import argparse
import random
from pathlib import Path

MOD = 1_000_000_007


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 14)
    points = [(rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(1, 12))
              for _ in range(n)]
    best = -1
    ways = 0
    for mask in range(1, 1 << n):
        chosen = [i for i in range(n) if mask >> i & 1]
        if all(points[a][0] < points[b][0] and points[a][1] < points[b][1]
               for a, b in zip(chosen, chosen[1:])):
            score = sum(points[i][2] for i in chosen)
            if score > best:
                best, ways = score, 1
            elif score == best:
                ways += 1
    text = f"{n}\n" + "".join(f"{x} {y} {w}\n" for x, y, w in points)
    return text, f"{best} {ways % MOD}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
