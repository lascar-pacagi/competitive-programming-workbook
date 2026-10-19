import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[:2]
    next_vertex = array('i', (x - 1 for x in data[2:2 + n]))
    value = data[2 + n:2 + 2 * n]
    index = 2 + 2 * n
    levels = 61
    up = [next_vertex]
    first_minimum = (value[next_vertex[v]] for v in range(n))
    minimum = [array('q', first_minimum)]
    for level in range(1, levels):
        previous_up = up[level - 1]
        previous_minimum = minimum[level - 1]
        up.append(array('i', [previous_up[p] for p in previous_up]))
        destinations = (previous_minimum[p] for p in previous_up)
        minimum.append(array('q', [
            a if a < b else b
            for a, b in zip(previous_minimum, destinations)
        ]))
    output = []
    for _ in range(q):
        vertex = data[index] - 1
        steps = data[index + 1]
        index += 2
        answer = value[vertex]
        while steps:
            # Consume just the set bits, in increasing jump order.
            bit = (steps & -steps).bit_length() - 1
            block_minimum = minimum[bit][vertex]
            if block_minimum < answer:
                answer = block_minimum
            vertex = up[bit][vertex]
            steps &= steps - 1
        output.append(f'{vertex + 1} {answer}')
    sys.stdout.write('\n'.join(output))
if __name__ == '__main__':
    main()
