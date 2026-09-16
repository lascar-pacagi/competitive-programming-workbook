import argparse
import math
import random
from pathlib import Path


def make_case(rng):
    n = rng.randint(1, 30)
    q = rng.randint(1, 60)
    values = [rng.randint(-20, 20) for _ in range(n)]
    current = values[:]
    operations = []
    answers = []

    for operation_index in range(q):
        left = rng.randint(1, n)
        right = rng.randint(left, n)
        must_query = operation_index == q - 1 and not answers
        if not must_query and rng.random() < 0.55:
            delta = rng.randint(-10, 10)
            operations.append(f"1 {left} {right} {delta}")
            for index in range(left - 1, right):
                current[index] += delta
        else:
            operations.append(f"2 {left} {right}")
            answer = 0
            for value in current[left - 1:right]:
                answer = math.gcd(answer, abs(value))
            answers.append(str(answer))

    input_text = (
        f"{n} {q}\n"
        + " ".join(map(str, values))
        + "\n"
        + "\n".join(operations)
        + "\n"
    )
    output_text = "\n".join(answers) + "\n"
    return input_text, output_text


def make_scale_case():
    n = 100_000
    repetitions = 50_000
    operations = []
    answers = []
    for value in range(1, repetitions + 1):
        operations.append(f"1 1 {n // 2} 1")
        operations.append(f"2 1 {n}")
        answers.append(str(value))

    input_text = (
        f"{n} {2 * repetitions}\n"
        + "0 " * (n - 1)
        + "0\n"
        + "\n".join(operations)
        + "\n"
    )
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
