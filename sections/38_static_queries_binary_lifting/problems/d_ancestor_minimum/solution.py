import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    labels = [0] + data[2:2 + n]
    index = 2 + n
    log = max(1, n.bit_length())
    infinity = 10**30
    up = [[0] * (n + 1) for _ in range(log)]
    minimum = [[infinity] * (n + 1) for _ in range(log)]
    for node in range(2, n + 1):
        up[0][node] = data[index]
        index += 1
    for node in range(1, n + 1):
        parent = up[0][node]
        parent_label = labels[parent] if parent else infinity
        minimum[0][node] = min(labels[node], parent_label)

    for bit in range(1, log):
        previous_up = up[bit - 1]
        previous_minimum = minimum[bit - 1]
        for node in range(1, n + 1):
            middle = previous_up[node]
            up[bit][node] = previous_up[middle]
            minimum[bit][node] = min(
                previous_minimum[node],
                previous_minimum[middle],
            )

    output: list[str] = []
    for _ in range(q):
        node = data[index]
        distance = data[index + 1]
        index += 2
        answer = labels[node]
        exists = True
        bit = 0
        while distance:
            if distance & 1:
                if bit >= log or up[bit][node] == 0:
                    exists = False
                    break
                answer = min(answer, minimum[bit][node])
                node = up[bit][node]
            distance >>= 1
            bit += 1
        output.append(str(answer if exists else -1))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
