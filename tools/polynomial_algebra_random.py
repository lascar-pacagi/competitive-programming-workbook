"""Independent small oracles for Sections 88--90."""
import argparse
import random
from pathlib import Path

MOD = 998244353


def multiply(a, b, n=None):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] = (result[i + j] + x * y) % MOD
    return result if n is None else (result + [0] * n)[:n]


def inverse(a, n):
    result = [pow(a[0], MOD - 2, MOD)]
    for degree in range(1, n):
        value = sum(a[i] * result[degree - i]
                    for i in range(1, min(degree + 1, len(a))))
        result.append(-value * result[0] % MOD)
    return result


def logarithm(a, n):
    quotient = multiply(
        [i * a[i] % MOD for i in range(1, len(a))], inverse(a, n), n - 1
    )
    return [0] + [quotient[i - 1] * pow(i, MOD - 2, MOD) % MOD
                  for i in range(1, n)]


def exponential(a, n):
    result = [1]
    for degree in range(1, n):
        value = sum(k * a[k] * result[degree - k]
                    for k in range(1, degree + 1))
        result.append(value * pow(degree, MOD - 2, MOD) % MOD)
    return result


def square_root(a, n):
    result = [1]
    half = (MOD + 1) // 2
    for degree in range(1, n):
        known = sum(result[i] * result[degree - i]
                    for i in range(1, degree))
        result.append((a[degree] - known) * half % MOD)
    return result


def evaluate(poly, x):
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % MOD
    return value


def interpolate(xs, ys):
    n = len(xs)
    answer = [0] * n
    for i in range(n):
        basis = [1]
        denominator = 1
        for j in range(n):
            if i == j:
                continue
            basis = multiply(basis, [-xs[j] % MOD, 1])
            denominator = denominator * (xs[i] - xs[j]) % MOD
        scale = ys[i] * pow(denominator, MOD - 2, MOD) % MOD
        for degree, coefficient in enumerate(basis):
            answer[degree] = (answer[degree] + scale * coefficient) % MOD
    return answer


def case(kind, rng):
    if kind in {"xor", "orconv", "subset", "cover"}:
        k = rng.randint(0, 5)
        size = 1 << k
        a = [rng.randrange(30) for _ in range(size)]
        b = [rng.randrange(30) for _ in range(size)]
        answer = [0] * size
        for x in range(size):
            for y in range(size):
                if kind == "xor":
                    target = x ^ y
                elif kind == "orconv":
                    target = x | y
                elif x & y:
                    continue
                else:
                    target = x | y
                answer[target] = (answer[target] + a[x] * b[y]) % MOD
        text = f"{k}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)) + "\n"
        return text, " ".join(map(str, answer)) + "\n"

    n = rng.randint(1, 15)
    if kind in {"evaluate", "archive_eval"}:
        q = rng.randint(1, 15)
        poly = [rng.randrange(40) for _ in range(n)]
        xs = [rng.randrange(15) for _ in range(q)]
        text = f"{n} {q}\n" + " ".join(map(str, poly)) + "\n" + " ".join(map(str, xs)) + "\n"
        return text, " ".join(str(evaluate(poly, x)) for x in xs) + "\n"
    if kind in {"interpolate", "recover"}:
        xs = rng.sample(range(40), n)
        poly = [rng.randrange(40) for _ in range(n)]
        ys = [evaluate(poly, x) for x in xs]
        pairs = list(zip(xs, ys))
        rng.shuffle(pairs)
        return f"{n}\n" + "".join(f"{x} {y}\n" for x, y in pairs), " ".join(map(str, poly)) + "\n"

    a = [rng.randrange(30) for _ in range(n)]
    if kind == "inverse":
        a[0] = rng.randrange(1, 30)
        answer = inverse(a, n)
    elif kind in {"log", "connected"}:
        a[0] = 1
        answer = logarithm(a, n)
    elif kind == "exp":
        a[0] = 0
        answer = exponential(a, n)
    elif kind == "sqrt":
        root = [1] + [rng.randrange(30) for _ in range(n - 1)]
        a = multiply(root, root, n)
        answer = root
    elif kind == "rational":
        q = [rng.randrange(1, 30)] + [rng.randrange(30) for _ in range(n - 1)]
        answer = multiply(a, inverse(q, n), n)
        text = f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, q)) + "\n"
        return text, " ".join(map(str, answer)) + "\n"
    else:
        raise ValueError(kind)
    return f"{n}\n" + " ".join(map(str, a)) + "\n", " ".join(map(str, answer)) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kind")
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        problem_input, expected = case(args.kind, rng)
        stem = args.out_dir / f"case{index:03d}"
        stem.with_suffix(".in").write_text(problem_input)
        stem.with_suffix(".out").write_text(expected)


if __name__ == "__main__":
    main()
