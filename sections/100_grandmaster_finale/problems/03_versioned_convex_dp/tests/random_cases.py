import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    q = rng.randint(1, 90)
    lines = [[(0, 0, 0)]]
    operations = []
    answers = []
    for version in range(1, q + 1):
        parent = rng.randrange(version)
        inherited = lines[parent]
        if rng.random() < 0.55:
            m = rng.randint(-20, 20)
            b = rng.randint(-40, 40)
            operations.append(f"{parent} A {m} {b}")
            lines.append(inherited + [(m, b, version)])
        else:
            x = rng.randint(-25, 25)
            operations.append(f"{parent} Q {x}")
            lines.append(inherited)
            value, identifier = min((m * x + b, identifier)
                                    for m, b, identifier in inherited)
            answers.append((value, identifier))
    return (f"{q}\n" + "\n".join(operations) + "\n",
            "".join(f"{value} {identifier}\n" for value, identifier in answers))


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
