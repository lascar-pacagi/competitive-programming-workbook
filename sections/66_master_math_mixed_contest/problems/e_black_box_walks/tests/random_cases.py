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
        n = rng.randint(1, 7)
        m = rng.randint(0, 20)
        length = rng.randint(0, 35)
        start, target = rng.randrange(n), rng.randrange(n)
        edges = [(rng.randrange(n), rng.randrange(n), rng.randint(0, 20)) for _ in range(m)]
        state = [0] * n
        state[start] = 1
        for _ in range(length):
            nxt = [0] * n
            for u, v, weight in edges:
                nxt[v] = (nxt[v] + state[u] * weight) % MOD
            state = nxt
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{n} {m} {length} {start+1} {target+1}\n"
            + "\n".join(f"{u+1} {v+1} {w}" for u, v, w in edges) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{state[target]}\n")


if __name__ == "__main__":
    main()
