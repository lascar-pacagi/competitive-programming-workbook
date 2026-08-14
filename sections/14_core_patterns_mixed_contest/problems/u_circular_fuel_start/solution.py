import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    fuel = data[1:n + 1]
    cost = data[n + 1:]
    total = tank = candidate = 0
    for i, (received, spent) in enumerate(zip(fuel, cost)):
        gain = received - spent
        total += gain
        tank += gain
        if tank < 0:
            candidate = i + 1
            tank = 0
    print(-1 if total < 0 else candidate)


if __name__ == "__main__":
    main()
