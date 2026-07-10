import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    teams = int(next(it))
    problems = int(next(it))
    submissions = int(next(it))
    solved = [[False] * (problems + 1) for _ in range(teams + 1)]
    wrong = [[0] * (problems + 1) for _ in range(teams + 1)]
    solved_count = [0] * (teams + 1)
    penalty = [0] * (teams + 1)

    for _ in range(submissions):
        minute = int(next(it))
        team = int(next(it))
        problem = int(next(it))
        verdict = next(it)
        if solved[team][problem]:
            continue
        if verdict == b"W":
            wrong[team][problem] += 1
        else:
            solved[team][problem] = True
            solved_count[team] += 1
            penalty[team] += minute + 20 * wrong[team][problem]

    order = sorted(range(1, teams + 1), key=lambda team: (-solved_count[team], penalty[team], team))
    print("\n".join(f"{team} {solved_count[team]} {penalty[team]}" for team in order))


if __name__ == "__main__":
    main()
