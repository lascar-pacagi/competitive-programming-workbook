import argparse
import random
from pathlib import Path


def make_case(rng):
    q = rng.randint(1, 100)
    current = {}
    next_id = 1
    reusable = []
    operations = []
    answers = []

    for operation_index in range(q):
        choice = rng.random()
        must_pop = operation_index == q - 1 and not answers
        if not must_pop and (not current or choice < 0.42):
            if reusable and rng.random() < 0.3:
                identifier = reusable.pop(rng.randrange(len(reusable)))
            else:
                identifier = next_id
                next_id += 1
            priority = rng.randint(-15, 15)
            current[identifier] = priority
            operations.append(f"A {identifier} {priority}")
        elif not must_pop and choice < 0.72:
            identifier = rng.choice(list(current))
            priority = rng.randint(-15, 15)
            current[identifier] = priority
            operations.append(f"U {identifier} {priority}")
        else:
            operations.append("P")
            if current:
                best = min(current, key=lambda item: (-current[item], item))
                answers.append(str(best))
                del current[best]
                reusable.append(best)
            else:
                answers.append("-1")

    input_text = f"{q}\n" + "\n".join(operations) + "\n"
    output_text = "\n".join(answers) + "\n"
    return input_text, output_text


def make_scale_case():
    task_count = 100_000
    changed_count = 50_000
    operations = []
    answers = []

    for identifier in range(1, task_count + 1):
        operations.append(f"A {identifier} {identifier}")
    for identifier in range(1, changed_count + 1):
        operations.append(f"U {identifier} {200_000 + identifier}")
    for identifier in range(changed_count, 0, -1):
        operations.append("P")
        answers.append(str(identifier))

    input_text = f"{len(operations)}\n" + "\n".join(operations) + "\n"
    output_text = "\n".join(answers) + "\n"
    return input_text, output_text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        if case_id == 0:
            input_text, output_text = make_scale_case()
        else:
            input_text, output_text = make_case(rng)
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(input_text)
        (args.out_dir / f"{stem}.out").write_text(output_text)


if __name__ == "__main__":
    main()
