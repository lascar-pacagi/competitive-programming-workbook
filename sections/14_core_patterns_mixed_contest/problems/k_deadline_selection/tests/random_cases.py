import argparse
import itertools
import random
from pathlib import Path


def feasible(jobs):
    total = 0
    for duration, deadline in sorted(jobs, key=lambda job: job[1]):
        total += duration
        if total > deadline:
            return False
    return True


def oracle(jobs):
    answer = 0
    for mask in range(1 << len(jobs)):
        chosen = [jobs[i] for i in range(len(jobs)) if mask >> i & 1]
        if len(chosen) > answer and feasible(chosen):
            answer = len(chosen)
    return answer


def greedy(jobs):
    import heapq
    selected = []
    total = 0
    for duration, deadline in sorted(jobs, key=lambda job: (job[1], job[0])):
        heapq.heappush(selected, -duration)
        total += duration
        if total > deadline:
            total += heapq.heappop(selected)
    return len(selected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        if case == 0:
            jobs = [(rng.randint(1, 1000), rng.randint(1, 10**9))
                    for _ in range(200000)]
            answer = greedy(jobs)
        else:
            jobs = [(rng.randint(1, 12), rng.randint(1, 40))
                    for _ in range(rng.randint(1, 16))]
            answer = oracle(jobs)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            str(len(jobs)) + "\n"
            + "\n".join(f"{duration} {deadline}" for duration, deadline in jobs)
            + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
