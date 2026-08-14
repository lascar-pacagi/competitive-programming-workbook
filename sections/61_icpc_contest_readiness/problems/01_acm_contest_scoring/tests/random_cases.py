from __future__ import annotations

import argparse
import random
from pathlib import Path


def score_case(text: str) -> str:
    values = text.split()
    it = iter(values)
    teams, problems, submissions = int(next(it)), int(next(it)), int(next(it))
    solved = [[False] * (problems + 1) for _ in range(teams + 1)]
    wrong = [[0] * (problems + 1) for _ in range(teams + 1)]
    solved_count = [0] * (teams + 1)
    penalty = [0] * (teams + 1)
    for _ in range(submissions):
        minute, team, problem = int(next(it)), int(next(it)), int(next(it))
        verdict = next(it)
        if solved[team][problem]:
            continue
        if verdict == "W":
            wrong[team][problem] += 1
        else:
            solved[team][problem] = True
            solved_count[team] += 1
            penalty[team] += minute + 20 * wrong[team][problem]
    order = sorted(range(1, teams + 1), key=lambda t: (-solved_count[t], penalty[t], t))
    return "\n".join(f"{t} {solved_count[t]} {penalty[t]}" for t in order) + "\n"


def make_case(rng: random.Random) -> str:
    teams, problems = rng.randint(1, 7), rng.randint(1, 6)
    submissions = rng.randint(0, 60)
    minute = 0
    lines = [f"{teams} {problems} {submissions}"]
    for _ in range(submissions):
        minute += rng.randint(0, 12)
        lines.append(
            f"{minute} {rng.randint(1, teams)} {rng.randint(1, problems)} "
            f"{rng.choice(['W', 'W', 'A'])}"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case{case_id:03}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case{case_id:03}.out").write_text(score_case(case), encoding="utf-8")


if __name__ == "__main__":
    main()
