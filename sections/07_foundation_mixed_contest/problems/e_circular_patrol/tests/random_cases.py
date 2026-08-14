import argparse
import random
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        tests = rng.randint(1, 12)
        lines = [str(tests)]
        out = []
        for _ in range(tests):
            n = rng.randint(1, 20)
            p = rng.randint(1, n)
            commands = "".join(rng.choice("LR") for _ in range(rng.randint(1, 40)))
            position = p - 1
            seen = {position}
            for command in commands:
                position = (position + (1 if command == "R" else -1)) % n
                seen.add(position)
            lines.append(f"{n} {p} {commands}")
            out.append(f"{position + 1} {len(seen)}")
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
