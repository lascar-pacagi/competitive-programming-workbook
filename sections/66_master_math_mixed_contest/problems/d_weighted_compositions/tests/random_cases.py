import argparse
import random
from pathlib import Path

MOD = 998_244_353


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(1, 9)
        target = rng.randint(0, 35)
        choices = [(rng.randint(1, 8), rng.randint(0, 7)) for _ in range(n)]
        dp = [1] + [0] * target
        for weight, cap in choices:
            nxt = [0] * (target + 1)
            for total, ways in enumerate(dp):
                for count in range(cap + 1):
                    new_total = total + count * weight
                    if new_total > target:
                        break
                    nxt[new_total] = (nxt[new_total] + ways) % MOD
            dp = nxt
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{n} {target}\n" + "\n".join(f"{w} {a}" for w, a in choices) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{dp[target]}\n")


if __name__ == "__main__":
    main()
