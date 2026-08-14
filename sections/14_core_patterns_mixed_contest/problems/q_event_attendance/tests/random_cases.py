import argparse
import random
from pathlib import Path


def oracle(events):
    match = {}

    def augment(event, seen):
        start, finish = events[event]
        for day in range(start, finish + 1):
            if day in seen:
                continue
            seen.add(day)
            if day not in match or augment(match[day], seen):
                match[day] = event
                return True
        return False

    answer = 0
    for event in range(len(events)):
        answer += augment(event, set())
    return answer


def greedy(events):
    import heapq
    events = sorted(events)
    finishes = []
    index = answer = 0
    day = 0
    while index < len(events) or finishes:
        if not finishes:
            day = max(day, events[index][0])
        while index < len(events) and events[index][0] <= day:
            heapq.heappush(finishes, events[index][1])
            index += 1
        while finishes and finishes[0] < day:
            heapq.heappop(finishes)
        if finishes:
            heapq.heappop(finishes)
            answer += 1
            day += 1
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[(1, 1)], [(1, 1), (1, 1)], [(1, 3), (1, 3), (1, 3)],
             [(10, 10), (1, 2), (2, 2)], [(1, 100), (2, 2), (2, 3)]]
    for case in range(args.count):
        if case < len(fixed):
            events = fixed[case]
        elif case == len(fixed):
            events = [(rng.randint(1, 10**9 - 1000), 0)
                      for _ in range(200000)]
            events = [(start, start + rng.randint(0, 1000))
                      for start, _ in events]
        else:
            events = []
            for _ in range(rng.randint(1, 13)):
                start = rng.randint(1, 12)
                events.append((start, rng.randint(start, 15)))
        answer = greedy(events) if len(events) > 20 else oracle(events)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            str(len(events)) + "\n"
            + "\n".join(f"{start} {finish}" for start, finish in events)
            + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
