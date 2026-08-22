import argparse
import random
from pathlib import Path

MOD = 1_000_000_007


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 8)
    q = rng.randint(1, 55)
    operations = []
    active = {}
    answers = []

    for operation_id in range(1, q + 1):
        choice = rng.random()
        if operation_id == q:
            operations.append("?")
            valid = 0
            for mask in range(1 << n):
                if all((((mask >> u) ^ (mask >> v)) & 1) == parity
                       for u, v, parity in active.values()):
                    valid += 1
            answers.append(valid % MOD)
        elif active and choice < 0.25:
            identifier = rng.choice(list(active))
            operations.append(f"- {identifier}")
            del active[identifier]
        elif choice < 0.68:
            u = rng.randrange(n)
            v = rng.randrange(n)
            parity = rng.randrange(2)
            operations.append(f"+ {u + 1} {v + 1} {parity}")
            active[operation_id] = (u, v, parity)
        else:
            operations.append("?")
            valid = 0
            for mask in range(1 << n):
                if all((((mask >> u) ^ (mask >> v)) & 1) == parity
                       for u, v, parity in active.values()):
                    valid += 1
            answers.append(valid % MOD)

    text = f"{n} {q}\n" + "\n".join(operations) + "\n"
    return text, "\n".join(map(str, answers)) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{index:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
