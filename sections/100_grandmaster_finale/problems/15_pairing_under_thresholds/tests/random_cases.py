import argparse
import random
from functools import lru_cache
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(2, 10)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    m = rng.randint(0, min(18, len(possible) + 4))
    edges = []
    for _ in range(m):
        u, v = rng.choice(possible)
        edges.append((u, v, rng.randint(1, 20)))
    q = rng.randint(1, 12)
    queries = [rng.randint(1, n // 2) for _ in range(q)]
    thresholds = sorted({difficulty for _, _, difficulty in edges})

    def rank(limit: int) -> int:
        adjacency = [0] * n
        for u, v, difficulty in edges:
            if difficulty <= limit:
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u

        @lru_cache(None)
        def dp(mask: int) -> int:
            if not mask:
                return 0
            bit = mask & -mask
            u = bit.bit_length() - 1
            rest = mask ^ bit
            answer = dp(rest)
            candidates = adjacency[u] & rest
            while candidates:
                other = candidates & -candidates
                answer = max(answer, 1 + dp(rest ^ other))
                candidates ^= other
            return answer

        return dp((1 << n) - 1)

    ranks = [(difficulty, rank(difficulty)) for difficulty in thresholds]
    answers = []
    for k in queries:
        answer = next((difficulty for difficulty, size in ranks if size >= k), -1)
        answers.append(answer)
    text = f"{n} {m} {q}\n"
    text += "".join(f"{u + 1} {v + 1} {difficulty}\n"
                    for u, v, difficulty in edges)
    text += "".join(f"{k}\n" for k in queries)
    return text, "".join(f"{answer}\n" for answer in answers)


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
