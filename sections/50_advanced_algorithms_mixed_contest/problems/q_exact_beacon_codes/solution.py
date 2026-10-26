import sys


def count_subsets(values, wanted_count, target):
    middle = len(values) // 2
    left, right = values[:middle], values[middle:]
    frequency = [{} for _ in range(len(left) + 1)]

    def collect(i, used, code):
        if used > wanted_count:
            return
        if i == len(left):
            group = frequency[used]
            group[code] = group.get(code, 0) + 1
            return
        collect(i + 1, used, code)
        collect(i + 1, used + 1, code ^ left[i])

    def combine(i, used, code):
        if used > wanted_count:
            return 0
        if i == len(right):
            need = wanted_count - used
            if 0 <= need < len(frequency):
                return frequency[need].get(target ^ code, 0)
            return 0
        return (combine(i + 1, used, code)
                + combine(i + 1, used + 1, code ^ right[i]))

    collect(0, 0, 0)
    return combine(0, 0, 0)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, target = data[:3]
    print(count_subsets(data[3:3 + n], k, target))


if __name__ == '__main__':
    main()
