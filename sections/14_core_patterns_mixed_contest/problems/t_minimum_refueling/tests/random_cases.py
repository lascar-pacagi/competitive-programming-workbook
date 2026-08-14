import argparse
import itertools
import random
from pathlib import Path


def oracle(destination, initial, stations):
    stations = sorted(stations)
    best = None
    for mask in range(1 << len(stations)):
        count = mask.bit_count()
        if best is not None and count >= best:
            continue
        reachable = initial
        valid = True
        for i, (position, fuel) in enumerate(stations):
            if mask >> i & 1:
                if position > reachable:
                    valid = False
                    break
                reachable += fuel
        if valid and reachable >= destination:
            best = count
    return -1 if best is None else best


def greedy(destination, reachable, stations):
    import heapq
    stations = sorted(stations)
    available = []
    index = stops = 0
    while reachable < destination:
        while index < len(stations) and stations[index][0] <= reachable:
            heapq.heappush(available, -stations[index][1])
            index += 1
        if not available:
            return -1
        reachable -= heapq.heappop(available)
        stops += 1
    return stops


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [(10, 10, []), (10, 0, []),
             (20, 5, [(5, 5), (10, 10)]),
             (100, 10, [(10, 10), (20, 10), (30, 100)])]
    for case in range(args.count):
        if case < len(fixed):
            destination, initial, stations = fixed[case]
        elif case == len(fixed):
            destination = 10**18
            initial = 1
            positions = sorted(rng.sample(range(1, 10**9), 200000))
            stations = [(position, rng.randint(1, 10**18))
                        for position in positions]
        else:
            destination = rng.randint(2, 45)
            positions = rng.sample(range(1, destination),
                                   rng.randint(0, min(10, destination - 1)))
            stations = [(position, rng.randint(1, 25))
                        for position in positions]
            initial = rng.randint(0, 20)
        answer = greedy(destination, initial, stations) if len(stations) > 15 \
            else oracle(destination, initial, stations)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{destination} {initial} {len(stations)}\n"
            + "\n".join(f"{position} {fuel}" for position, fuel in stations)
            + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
