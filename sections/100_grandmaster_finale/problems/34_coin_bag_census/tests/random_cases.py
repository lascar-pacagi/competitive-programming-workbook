import argparse
import random
from pathlib import Path

MOD = 998244353


def brute(S, ws):
    ways = [1] + [0] * S
    for w in ws:
        for s in range(w, S + 1):
            ways[s] = (ways[s] + ways[s - w]) % MOD
    return ways[1:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        S = rng.randint(1, 300)
        n = rng.randint(1, 40)
        top = rng.choice([3, 20, 400, 10**5])
        ws = [rng.randint(1, top) for _ in range(n)]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {S}\n{' '.join(map(str, ws))}\n")
        stem.with_suffix(".out").write_text(" ".join(map(str, brute(S, ws))) + "\n")


if __name__ == "__main__":
    main()
