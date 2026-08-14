from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def encode(bits: str) -> int:
    value = 0
    for index, bit in enumerate(bits):
        if bit == "1":
            value |= 1 << index
    return value


def shortest_distance(n: int, start: str, target: str) -> int:
    """Independent tiny oracle: BFS over the entire binary-string state graph."""
    source = encode(start)
    goal = encode(target)
    distance = {source: 0}
    queue = deque([source])
    while queue:
        state = queue.popleft()
        if state == goal:
            return distance[state]
        for index in range(n - 1):
            next_state = state ^ (1 << index) ^ (1 << (index + 1))
            if next_state not in distance:
                distance[next_state] = distance[state] + 1
                queue.append(next_state)
    return -1


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 8)
    start = "".join(rng.choice("01") for _ in range(n))
    target = "".join(rng.choice("01") for _ in range(n))
    answer = shortest_distance(n, start, target)
    return f"{n}\n{start}\n{target}\n", f"{answer}\n"


def scale_case() -> tuple[str, str]:
    """Flipping every edge once yields endpoint mismatches only."""
    n = 200_000
    start = "0" * n
    target = "1" + "0" * (n - 2) + "1"
    return f"{n}\n{start}\n{target}\n", f"{n - 1}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for number in range(args.count):
        case, expected = scale_case() if number == 0 else small_case(rng)
        (args.out_dir / f"case_{number:03d}.in").write_text(case)
        (args.out_dir / f"case_{number:03d}.out").write_text(expected)


if __name__ == "__main__":
    main()
