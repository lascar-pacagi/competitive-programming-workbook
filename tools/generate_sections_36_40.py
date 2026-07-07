"""Generate Sections 36-40 of the competitive programming course."""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"

HEADER = """---
title: "Competitive Programming"
subtitle: "{subtitle}"
author: "Competitive Programming Course"
date: last-modified
format:
  pdf:
    pdf-engine: xelatex
    documentclass: scrreprt
    papersize: a4
    toc: true
    toc-depth: 2
    number-sections: true
    colorlinks: true
    geometry:
      - margin=25mm
    include-in-header:
      text: |
        \\usepackage{{microtype}}
        \\usepackage{{amsmath}}
        \\usepackage{{booktabs}}
execute:
  enabled: false
---
"""


@dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    statement: str
    sample: str
    py: str
    cpp: str
    random_kind: str


@dataclass(frozen=True)
class Section:
    number: int
    slug: str
    title: str
    lesson: str
    practice: str
    problems: tuple[Problem, Problem, Problem]


def dedent(s: str) -> str:
    return textwrap.dedent(s).strip() + "\n"


RANDOM_CASES = r'''
from __future__ import annotations

import argparse
import random
import subprocess
import sys
from pathlib import Path


KIND = "__KIND__"
PROBLEM = Path(__file__).resolve().parents[1]


def expected(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(PROBLEM / "solution.py")],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def case_fenwick_sum(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    q = rng.randint(1, 60)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.55:
            i = rng.randint(1, n)
            x = rng.randint(-15, 15)
            ops.append(f"1 {i} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_inversions(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    a = [rng.randint(-30, 30) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


def case_range_add_point(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    q = rng.randint(1, 70)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.65:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.randint(-10, 10)
            ops.append(f"1 {l} {r} {x}")
        else:
            i = rng.randint(1, n)
            ops.append(f"2 {i}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_seg_min(rng: random.Random) -> str:
    n = rng.randint(1, 32)
    q = rng.randint(1, 70)
    a = [rng.randint(-50, 50) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.5:
            i = rng.randint(1, n)
            x = rng.randint(-50, 50)
            ops.append(f"1 {i} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_max_subarray(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    q = rng.randint(1, 60)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = [f"{rng.randint(1, n)} {rng.randint(-20, 20)}" for _ in range(q)]
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_lazy_sum(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    q = rng.randint(1, 70)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.6:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.randint(-15, 15)
            ops.append(f"1 {l} {r} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_static_min(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(-100, 100) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


def case_static_gcd(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 200) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


def case_kth_ancestor(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    q = rng.randint(1, 80)
    parents = [rng.randint(1, v - 1) for v in range(2, n + 1)]
    queries = [f"{rng.randint(1, n)} {rng.randint(0, n + 5)}" for _ in range(q)]
    return f"{n} {q}\n" + (" ".join(map(str, parents)) if parents else "") + "\n" + "\n".join(queries) + "\n"


def case_running_median(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    a = [rng.randint(-100, 100) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


def case_course_rooms(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    intervals = []
    for _ in range(n):
        l = rng.randint(0, 200)
        r = l + rng.randint(1, 40)
        intervals.append(f"{l} {r}")
    return f"{n}\n" + "\n".join(intervals) + "\n"


def case_pair_sums(rng: random.Random) -> str:
    n = rng.randint(1, 25)
    m = rng.randint(1, 25)
    k = rng.randint(1, min(80, n * m))
    a = sorted(rng.randint(-30, 30) for _ in range(n))
    b = sorted(rng.randint(-30, 30) for _ in range(m))
    return f"{n} {m} {k}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)) + "\n"


def case_hotel(rng: random.Random) -> str:
    n = rng.randint(1, 50)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 30) for _ in range(n)]
    req = [rng.randint(1, 40) for _ in range(q)]
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, req)) + "\n"


def case_list_removals(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    a = [rng.randint(-100, 100) for _ in range(n)]
    alive = n
    pos = []
    for _ in range(n):
        p = rng.randint(1, alive)
        pos.append(p)
        alive -= 1
    return f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, pos)) + "\n"


def case_mo_distinct(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 25) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


BUILDERS = {
    "fenwick_sum": case_fenwick_sum,
    "inversions": case_inversions,
    "range_add_point": case_range_add_point,
    "seg_min": case_seg_min,
    "max_subarray": case_max_subarray,
    "lazy_sum": case_lazy_sum,
    "static_min": case_static_min,
    "static_gcd": case_static_gcd,
    "kth_ancestor": case_kth_ancestor,
    "running_median": case_running_median,
    "course_rooms": case_course_rooms,
    "pair_sums": case_pair_sums,
    "hotel": case_hotel,
    "list_removals": case_list_removals,
    "mo_distinct": case_mo_distinct,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    builder = BUILDERS[KIND]
    for i in range(args.count):
        inp = builder(rng)
        stem = f"case{i:03d}"
        (args.out_dir / f"{stem}.in").write_text(inp, encoding="utf-8")
        (args.out_dir / f"{stem}.out").write_text(expected(inp), encoding="utf-8")


if __name__ == "__main__":
    main()
'''


PY_FENWICK_SUM = dedent(
    r'''
    import sys

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)
        def add(self, i, delta):
            while i <= self.n:
                self.bit[i] += delta
                i += i & -i
        def sum(self, i):
            res = 0
            while i > 0:
                res += self.bit[i]
                i -= i & -i
            return res
        def range_sum(self, l, r):
            return self.sum(r) - self.sum(l - 1)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        bit = Fenwick(n)
        for i, x in enumerate(a, 1):
            bit.add(i, x)
        idx = 2 + n
        out = []
        for _ in range(q):
            typ = data[idx]
            idx += 1
            if typ == 1:
                i, x = data[idx], data[idx + 1]
                idx += 2
                bit.add(i, x)
            else:
                l, r = data[idx], data[idx + 1]
                idx += 2
                out.append(str(bit.range_sum(l, r)))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_FENWICK_SUM = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct Fenwick {
        int n;
        vector<long long> bit;
        Fenwick(int n) : n(n), bit(n + 1, 0) {}
        void add(int i, long long delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        long long sum(int i) const {
            long long res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
        long long range_sum(int l, int r) const {
            return sum(r) - sum(l - 1);
        }
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        Fenwick bit(n);
        for (int i = 1; i <= n; i++) {
            long long x;
            cin >> x;
            bit.add(i, x);
        }
        while (q--) {
            int typ;
            cin >> typ;
            if (typ == 1) {
                int i;
                long long x;
                cin >> i >> x;
                bit.add(i, x);
            } else {
                int l, r;
                cin >> l >> r;
                cout << bit.range_sum(l, r) << '\n';
            }
        }
        return 0;
    }
    '''
)

PY_INVERSIONS = dedent(
    r'''
    import sys

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)
        def add(self, i, delta):
            while i <= self.n:
                self.bit[i] += delta
                i += i & -i
        def sum(self, i):
            res = 0
            while i > 0:
                res += self.bit[i]
                i -= i & -i
            return res

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        a = data[1:1 + n]
        values = {x: i + 1 for i, x in enumerate(sorted(set(a)))}
        bit = Fenwick(len(values))
        inv = 0
        seen = 0
        for x in a:
            rank = values[x]
            inv += seen - bit.sum(rank)
            bit.add(rank, 1)
            seen += 1
        print(inv)

    if __name__ == "__main__":
        main()
    '''
)

CPP_INVERSIONS = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n) : n(n), bit(n + 1, 0) {}
        void add(int i, int delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        int sum(int i) const {
            int res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n;
        if (!(cin >> n)) return 0;
        vector<long long> a(n), vals;
        for (long long &x : a) {
            cin >> x;
            vals.push_back(x);
        }
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        Fenwick bit((int)vals.size());
        long long inv = 0;
        for (int i = 0; i < n; i++) {
            int rank = int(lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin()) + 1;
            inv += i - bit.sum(rank);
            bit.add(rank, 1);
        }
        cout << inv << '\n';
        return 0;
    }
    '''
)

PY_RANGE_ADD_POINT = dedent(
    r'''
    import sys

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 2)
        def add(self, i, delta):
            while i <= self.n:
                self.bit[i] += delta
                i += i & -i
        def sum(self, i):
            res = 0
            while i > 0:
                res += self.bit[i]
                i -= i & -i
            return res

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        bit = Fenwick(n + 1)
        prev = 0
        for i, x in enumerate(a, 1):
            bit.add(i, x - prev)
            prev = x
        idx = 2 + n
        out = []
        for _ in range(q):
            typ = data[idx]
            idx += 1
            if typ == 1:
                l, r, x = data[idx], data[idx + 1], data[idx + 2]
                idx += 3
                bit.add(l, x)
                bit.add(r + 1, -x)
            else:
                i = data[idx]
                idx += 1
                out.append(str(bit.sum(i)))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_RANGE_ADD_POINT = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct Fenwick {
        int n;
        vector<long long> bit;
        Fenwick(int n) : n(n), bit(n + 2, 0) {}
        void add(int i, long long delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        long long sum(int i) const {
            long long res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        Fenwick bit(n + 1);
        long long prev = 0;
        for (int i = 1; i <= n; i++) {
            long long x;
            cin >> x;
            bit.add(i, x - prev);
            prev = x;
        }
        while (q--) {
            int typ;
            cin >> typ;
            if (typ == 1) {
                int l, r;
                long long x;
                cin >> l >> r >> x;
                bit.add(l, x);
                bit.add(r + 1, -x);
            } else {
                int i;
                cin >> i;
                cout << bit.sum(i) << '\n';
            }
        }
        return 0;
    }
    '''
)

PY_SEG_MIN = dedent(
    r'''
    import sys

    INF = 10**30

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        size = 1
        while size < n:
            size *= 2
        seg = [INF] * (2 * size)
        for i, x in enumerate(a):
            seg[size + i] = x
        for i in range(size - 1, 0, -1):
            seg[i] = min(seg[2 * i], seg[2 * i + 1])
        idx = 2 + n
        out = []
        for _ in range(q):
            typ, x, y = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            if typ == 1:
                p = size + x - 1
                seg[p] = y
                p //= 2
                while p:
                    seg[p] = min(seg[2 * p], seg[2 * p + 1])
                    p //= 2
            else:
                l, r = x - 1 + size, y + size
                ans = INF
                while l < r:
                    if l & 1:
                        ans = min(ans, seg[l])
                        l += 1
                    if r & 1:
                        r -= 1
                        ans = min(ans, seg[r])
                    l //= 2
                    r //= 2
                out.append(str(ans))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_SEG_MIN = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        int size = 1;
        while (size < n) size <<= 1;
        const long long INF = (1LL << 60);
        vector<long long> seg(2 * size, INF);
        for (int i = 0; i < n; i++) cin >> seg[size + i];
        for (int i = size - 1; i >= 1; i--) seg[i] = min(seg[2 * i], seg[2 * i + 1]);
        while (q--) {
            int typ, x, y;
            cin >> typ >> x >> y;
            if (typ == 1) {
                int p = size + x - 1;
                seg[p] = y;
                for (p >>= 1; p; p >>= 1) seg[p] = min(seg[2 * p], seg[2 * p + 1]);
            } else {
                int l = size + x - 1, r = size + y;
                long long ans = INF;
                while (l < r) {
                    if (l & 1) ans = min(ans, seg[l++]);
                    if (r & 1) ans = min(ans, seg[--r]);
                    l >>= 1;
                    r >>= 1;
                }
                cout << ans << '\n';
            }
        }
        return 0;
    }
    '''
)

PY_MAX_SUBARRAY = dedent(
    r'''
    import sys

    NEG = -10**30

    def merge(a, b):
        total = a[0] + b[0]
        pref = max(a[1], a[0] + b[1])
        suff = max(b[2], b[0] + a[2])
        best = max(a[3], b[3], a[2] + b[1])
        return (total, pref, suff, best)

    def leaf(x):
        return (x, x, x, x)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        size = 1
        while size < n:
            size *= 2
        neutral = (0, NEG, NEG, NEG)
        seg = [neutral] * (2 * size)
        for i, x in enumerate(a):
            seg[size + i] = leaf(x)
        for i in range(size - 1, 0, -1):
            seg[i] = merge(seg[2 * i], seg[2 * i + 1])
        idx = 2 + n
        out = []
        for _ in range(q):
            pos, val = data[idx], data[idx + 1]
            idx += 2
            p = size + pos - 1
            seg[p] = leaf(val)
            p //= 2
            while p:
                seg[p] = merge(seg[2 * p], seg[2 * p + 1])
                p //= 2
            out.append(str(seg[1][3]))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_MAX_SUBARRAY = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    const long long NEG = -(1LL << 60);

    struct Node {
        long long sum, pref, suff, best;
    };

    Node leaf(long long x) { return {x, x, x, x}; }
    Node merge(Node a, Node b) {
        return {
            a.sum + b.sum,
            max(a.pref, a.sum + b.pref),
            max(b.suff, b.sum + a.suff),
            max({a.best, b.best, a.suff + b.pref})
        };
    }

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        int size = 1;
        while (size < n) size <<= 1;
        Node neutral{0, NEG, NEG, NEG};
        vector<Node> seg(2 * size, neutral);
        for (int i = 0; i < n; i++) {
            long long x;
            cin >> x;
            seg[size + i] = leaf(x);
        }
        for (int i = size - 1; i >= 1; i--) seg[i] = merge(seg[2 * i], seg[2 * i + 1]);
        while (q--) {
            int pos;
            long long val;
            cin >> pos >> val;
            int p = size + pos - 1;
            seg[p] = leaf(val);
            for (p >>= 1; p; p >>= 1) seg[p] = merge(seg[2 * p], seg[2 * p + 1]);
            cout << seg[1].best << '\n';
        }
        return 0;
    }
    '''
)

PY_LAZY_SUM = dedent(
    r'''
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        size = 1
        while size < n:
            size *= 2
        seg = [0] * (2 * size)
        lazy = [0] * (2 * size)
        for i, x in enumerate(a):
            seg[size + i] = x
        for i in range(size - 1, 0, -1):
            seg[i] = seg[2 * i] + seg[2 * i + 1]
        def apply(v, length, delta):
            seg[v] += delta * length
            lazy[v] += delta
        def push(v, length):
            if lazy[v] and v < size:
                half = length // 2
                apply(2 * v, half, lazy[v])
                apply(2 * v + 1, half, lazy[v])
                lazy[v] = 0
        def add(v, tl, tr, l, r, x):
            if l <= tl and tr <= r:
                apply(v, tr - tl + 1, x)
                return
            push(v, tr - tl + 1)
            tm = (tl + tr) // 2
            if l <= tm:
                add(2 * v, tl, tm, l, r, x)
            if tm < r:
                add(2 * v + 1, tm + 1, tr, l, r, x)
            seg[v] = seg[2 * v] + seg[2 * v + 1]
        def query(v, tl, tr, l, r):
            if l <= tl and tr <= r:
                return seg[v]
            push(v, tr - tl + 1)
            tm = (tl + tr) // 2
            ans = 0
            if l <= tm:
                ans += query(2 * v, tl, tm, l, r)
            if tm < r:
                ans += query(2 * v + 1, tm + 1, tr, l, r)
            return ans
        idx = 2 + n
        out = []
        for _ in range(q):
            typ = data[idx]
            idx += 1
            if typ == 1:
                l, r, x = data[idx], data[idx + 1], data[idx + 2]
                idx += 3
                add(1, 1, size, l, r, x)
            else:
                l, r = data[idx], data[idx + 1]
                idx += 2
                out.append(str(query(1, 1, size, l, r)))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_LAZY_SUM = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct SegTree {
        int n;
        vector<long long> seg, lazy;
        SegTree(const vector<long long>& a) {
            n = 1;
            while (n < (int)a.size()) n <<= 1;
            seg.assign(2 * n, 0);
            lazy.assign(2 * n, 0);
            for (int i = 0; i < (int)a.size(); i++) seg[n + i] = a[i];
            for (int i = n - 1; i >= 1; i--) seg[i] = seg[2 * i] + seg[2 * i + 1];
        }
        void apply(int v, int len, long long x) {
            seg[v] += x * len;
            lazy[v] += x;
        }
        void push(int v, int len) {
            if (lazy[v] && v < n) {
                int half = len / 2;
                apply(2 * v, half, lazy[v]);
                apply(2 * v + 1, half, lazy[v]);
                lazy[v] = 0;
            }
        }
        void add(int v, int tl, int tr, int l, int r, long long x) {
            if (l <= tl && tr <= r) {
                apply(v, tr - tl + 1, x);
                return;
            }
            push(v, tr - tl + 1);
            int tm = (tl + tr) / 2;
            if (l <= tm) add(2 * v, tl, tm, l, r, x);
            if (tm < r) add(2 * v + 1, tm + 1, tr, l, r, x);
            seg[v] = seg[2 * v] + seg[2 * v + 1];
        }
        long long query(int v, int tl, int tr, int l, int r) {
            if (l <= tl && tr <= r) return seg[v];
            push(v, tr - tl + 1);
            int tm = (tl + tr) / 2;
            long long ans = 0;
            if (l <= tm) ans += query(2 * v, tl, tm, l, r);
            if (tm < r) ans += query(2 * v + 1, tm + 1, tr, l, r);
            return ans;
        }
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        SegTree st(a);
        while (q--) {
            int typ, l, r;
            cin >> typ >> l >> r;
            if (typ == 1) {
                long long x;
                cin >> x;
                st.add(1, 1, st.n, l, r, x);
            } else {
                cout << st.query(1, 1, st.n, l, r) << '\n';
            }
        }
        return 0;
    }
    '''
)

PY_STATIC_MIN = dedent(
    r'''
    import sys, math

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1
        st = [a]
        k = 1
        while (1 << k) <= n:
            prev = st[-1]
            length = 1 << (k - 1)
            st.append([min(prev[i], prev[i + length]) for i in range(n - (1 << k) + 1)])
            k += 1
        idx = 2 + n
        out = []
        for _ in range(q):
            l, r = data[idx] - 1, data[idx + 1] - 1
            idx += 2
            k = log[r - l + 1]
            out.append(str(min(st[k][l], st[k][r - (1 << k) + 1])))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_STATIC_MIN = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        vector<int> lg(n + 1);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
        int K = lg[n] + 1;
        vector<vector<long long>> st(K, vector<long long>(n));
        for (int i = 0; i < n; i++) cin >> st[0][i];
        for (int k = 1; k < K; k++) {
            for (int i = 0; i + (1 << k) <= n; i++) {
                st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
        while (q--) {
            int l, r;
            cin >> l >> r;
            --l; --r;
            int k = lg[r - l + 1];
            cout << min(st[k][l], st[k][r - (1 << k) + 1]) << '\n';
        }
        return 0;
    }
    '''
)

PY_STATIC_GCD = dedent(
    r'''
    import math
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1
        st = [a]
        k = 1
        while (1 << k) <= n:
            prev = st[-1]
            length = 1 << (k - 1)
            st.append([math.gcd(prev[i], prev[i + length]) for i in range(n - (1 << k) + 1)])
            k += 1
        idx = 2 + n
        out = []
        for _ in range(q):
            l, r = data[idx] - 1, data[idx + 1] - 1
            idx += 2
            k = log[r - l + 1]
            out.append(str(math.gcd(st[k][l], st[k][r - (1 << k) + 1])))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_STATIC_GCD = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        vector<int> lg(n + 1);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
        int K = lg[n] + 1;
        vector<vector<long long>> st(K, vector<long long>(n));
        for (int i = 0; i < n; i++) cin >> st[0][i];
        for (int k = 1; k < K; k++) {
            for (int i = 0; i + (1 << k) <= n; i++) {
                st[k][i] = gcd(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
        while (q--) {
            int l, r;
            cin >> l >> r;
            --l; --r;
            int k = lg[r - l + 1];
            cout << gcd(st[k][l], st[k][r - (1 << k) + 1]) << '\n';
        }
        return 0;
    }
    '''
)

PY_KTH_ANCESTOR = dedent(
    r'''
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        LOG = max(1, (n + 5).bit_length())
        up = [[0] * (n + 1) for _ in range(LOG)]
        idx = 2
        for v in range(2, n + 1):
            up[0][v] = data[idx]
            idx += 1
        for k in range(1, LOG):
            for v in range(1, n + 1):
                up[k][v] = up[k - 1][up[k - 1][v]]
        out = []
        for _ in range(q):
            v, dist = data[idx], data[idx + 1]
            idx += 2
            bit = 0
            while dist and v:
                if dist & 1:
                    v = up[bit][v] if bit < LOG else 0
                dist >>= 1
                bit += 1
            out.append(str(v if v else -1))
        print("\n".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_KTH_ANCESTOR = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        int LOG = 1;
        while ((1 << LOG) <= n + 5) LOG++;
        vector<vector<int>> up(LOG, vector<int>(n + 1, 0));
        for (int v = 2; v <= n; v++) cin >> up[0][v];
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
        }
        while (q--) {
            int v;
            long long dist;
            cin >> v >> dist;
            for (int k = 0; k < LOG && v; k++) {
                if (dist & (1LL << k)) v = up[k][v];
            }
            cout << (v ? v : -1) << '\n';
        }
        return 0;
    }
    '''
)

PY_RUNNING_MEDIAN = dedent(
    r'''
    import heapq
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        low, high = [], []
        out = []
        for x in data[1:1 + n]:
            if not low or x <= -low[0]:
                heapq.heappush(low, -x)
            else:
                heapq.heappush(high, x)
            if len(low) < len(high):
                heapq.heappush(low, -heapq.heappop(high))
            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            out.append(str(-low[0]))
        print(" ".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_RUNNING_MEDIAN = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n;
        if (!(cin >> n)) return 0;
        priority_queue<long long> low;
        priority_queue<long long, vector<long long>, greater<long long>> high;
        for (int i = 0; i < n; i++) {
            long long x;
            cin >> x;
            if (low.empty() || x <= low.top()) low.push(x);
            else high.push(x);
            if (low.size() < high.size()) {
                low.push(high.top());
                high.pop();
            }
            if (low.size() > high.size() + 1) {
                high.push(low.top());
                low.pop();
            }
            if (i) cout << ' ';
            cout << low.top();
        }
        cout << '\n';
        return 0;
    }
    '''
)

PY_COURSE_ROOMS = dedent(
    r'''
    import heapq
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        intervals = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]
        intervals.sort()
        heap = []
        ans = 0
        for l, r in intervals:
            while heap and heap[0] <= l:
                heapq.heappop(heap)
            heapq.heappush(heap, r)
            ans = max(ans, len(heap))
        print(ans)

    if __name__ == "__main__":
        main()
    '''
)

CPP_COURSE_ROOMS = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n;
        if (!(cin >> n)) return 0;
        vector<pair<int,int>> intervals(n);
        for (auto &[l, r] : intervals) cin >> l >> r;
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> pq;
        int ans = 0;
        for (auto [l, r] : intervals) {
            while (!pq.empty() && pq.top() <= l) pq.pop();
            pq.push(r);
            ans = max(ans, (int)pq.size());
        }
        cout << ans << '\n';
        return 0;
    }
    '''
)

PY_PAIR_SUMS = dedent(
    r'''
    import heapq
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, m, k = data[0], data[1], data[2]
        a = data[3:3 + n]
        b = data[3 + n:3 + n + m]
        heap = [(a[i] + b[0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        out = []
        for _ in range(k):
            s, i, j = heapq.heappop(heap)
            out.append(str(s))
            if j + 1 < m:
                heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
        print(" ".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_PAIR_SUMS = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, m, k;
        if (!(cin >> n >> m >> k)) return 0;
        vector<long long> a(n), b(m);
        for (auto &x : a) cin >> x;
        for (auto &x : b) cin >> x;
        using State = tuple<long long,int,int>;
        priority_queue<State, vector<State>, greater<State>> pq;
        for (int i = 0; i < n; i++) pq.emplace(a[i] + b[0], i, 0);
        for (int t = 0; t < k; t++) {
            auto [s, i, j] = pq.top();
            pq.pop();
            if (t) cout << ' ';
            cout << s;
            if (j + 1 < m) pq.emplace(a[i] + b[j + 1], i, j + 1);
        }
        cout << '\n';
        return 0;
    }
    '''
)

PY_HOTEL = dedent(
    r'''
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        req = data[2 + n:2 + n + q]
        size = 1
        while size < n:
            size *= 2
        seg = [0] * (2 * size)
        for i, x in enumerate(a):
            seg[size + i] = x
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])
        out = []
        for x in req:
            if seg[1] < x:
                out.append("0")
                continue
            v = 1
            while v < size:
                if seg[2 * v] >= x:
                    v *= 2
                else:
                    v = 2 * v + 1
            pos = v - size
            seg[v] -= x
            v //= 2
            while v:
                seg[v] = max(seg[2 * v], seg[2 * v + 1])
                v //= 2
            out.append(str(pos + 1))
        print(" ".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_HOTEL = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        int size = 1;
        while (size < n) size <<= 1;
        vector<long long> seg(2 * size, 0);
        for (int i = 0; i < n; i++) cin >> seg[size + i];
        for (int i = size - 1; i >= 1; i--) seg[i] = max(seg[2 * i], seg[2 * i + 1]);
        for (int qi = 0; qi < q; qi++) {
            long long x;
            cin >> x;
            int ans = 0;
            if (seg[1] >= x) {
                int v = 1;
                while (v < size) {
                    if (seg[2 * v] >= x) v *= 2;
                    else v = 2 * v + 1;
                }
                ans = v - size + 1;
                seg[v] -= x;
                for (v >>= 1; v; v >>= 1) seg[v] = max(seg[2 * v], seg[2 * v + 1]);
            }
            if (qi) cout << ' ';
            cout << ans;
        }
        cout << '\n';
        return 0;
    }
    '''
)

PY_LIST_REMOVALS = dedent(
    r'''
    import sys

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)
        def add(self, i, delta):
            while i <= self.n:
                self.bit[i] += delta
                i += i & -i
        def kth(self, k):
            pos = 0
            bit = 1 << self.n.bit_length()
            while bit:
                nxt = pos + bit
                if nxt <= self.n and self.bit[nxt] < k:
                    pos = nxt
                    k -= self.bit[nxt]
                bit //= 2
            return pos + 1

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        a = data[1:1 + n]
        positions = data[1 + n:1 + 2 * n]
        bit = Fenwick(n)
        for i in range(1, n + 1):
            bit.add(i, 1)
        out = []
        for k in positions:
            idx = bit.kth(k)
            out.append(str(a[idx - 1]))
            bit.add(idx, -1)
        print(" ".join(out))

    if __name__ == "__main__":
        main()
    '''
)

CPP_LIST_REMOVALS = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n) : n(n), bit(n + 1, 0) {}
        void add(int i, int delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        int kth(int k) const {
            int pos = 0;
            int step = 1;
            while ((step << 1) <= n) step <<= 1;
            for (; step; step >>= 1) {
                int nxt = pos + step;
                if (nxt <= n && bit[nxt] < k) {
                    pos = nxt;
                    k -= bit[nxt];
                }
            }
            return pos + 1;
        }
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n;
        if (!(cin >> n)) return 0;
        vector<long long> a(n + 1);
        for (int i = 1; i <= n; i++) cin >> a[i];
        Fenwick bit(n);
        for (int i = 1; i <= n; i++) bit.add(i, 1);
        for (int t = 0; t < n; t++) {
            int k;
            cin >> k;
            int idx = bit.kth(k);
            if (t) cout << ' ';
            cout << a[idx];
            bit.add(idx, -1);
        }
        cout << '\n';
        return 0;
    }
    '''
)

PY_MO_DISTINCT = dedent(
    r'''
    import sys
    from collections import defaultdict

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, q = data[0], data[1]
        a = data[2:2 + n]
        idx = 2 + n
        block = max(1, int(n ** 0.5))
        queries = []
        for qi in range(q):
            l, r = data[idx] - 1, data[idx + 1] - 1
            idx += 2
            queries.append((l, r, qi))
        queries.sort(key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1]))
        freq = defaultdict(int)
        ans = [0] * q
        distinct = 0
        left, right = 0, -1
        for l, r, qi in queries:
            while right < r:
                right += 1
                freq[a[right]] += 1
                if freq[a[right]] == 1:
                    distinct += 1
            while right > r:
                freq[a[right]] -= 1
                if freq[a[right]] == 0:
                    distinct -= 1
                right -= 1
            while left < l:
                freq[a[left]] -= 1
                if freq[a[left]] == 0:
                    distinct -= 1
                left += 1
            while left > l:
                left -= 1
                freq[a[left]] += 1
                if freq[a[left]] == 1:
                    distinct += 1
            ans[qi] = distinct
        print("\n".join(map(str, ans)))

    if __name__ == "__main__":
        main()
    '''
)

CPP_MO_DISTINCT = dedent(
    r'''
    #include <bits/stdc++.h>
    using namespace std;

    struct Query {
        int l, r, id;
    };

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, q;
        if (!(cin >> n >> q)) return 0;
        vector<int> a(n), vals;
        for (int &x : a) {
            cin >> x;
            vals.push_back(x);
        }
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        for (int &x : a) x = int(lower_bound(vals.begin(), vals.end(), x) - vals.begin());
        vector<Query> queries(q);
        for (int i = 0; i < q; i++) {
            cin >> queries[i].l >> queries[i].r;
            --queries[i].l; --queries[i].r;
            queries[i].id = i;
        }
        int block = max(1, (int)sqrt(n));
        sort(queries.begin(), queries.end(), [&](const Query& A, const Query& B) {
            int ba = A.l / block, bb = B.l / block;
            if (ba != bb) return ba < bb;
            return (ba & 1) ? A.r > B.r : A.r < B.r;
        });
        vector<int> freq(vals.size(), 0), ans(q);
        int distinct = 0, l = 0, r = -1;
        auto add = [&](int pos) {
            if (freq[a[pos]]++ == 0) distinct++;
        };
        auto remove = [&](int pos) {
            if (--freq[a[pos]] == 0) distinct--;
        };
        for (auto qu : queries) {
            while (r < qu.r) add(++r);
            while (r > qu.r) remove(r--);
            while (l < qu.l) remove(l++);
            while (l > qu.l) add(--l);
            ans[qu.id] = distinct;
        }
        for (int x : ans) cout << x << '\n';
        return 0;
    }
    '''
)


SECTIONS_DATA: tuple[Section, ...] = (
    Section(
        36,
        "fenwick_trees",
        "Fenwick Trees",
        dedent(
            r'''
            # Fenwick trees without black boxes

            A Fenwick tree, also called a binary indexed tree, stores prefix
            information in an array `bit[1..n]`. The key idea is that index `i`
            owns a block whose length is the value of its lowest set bit:

            ```text
            lowbit(i) = i & -i

            bit[i] stores the sum of:
            i-lowbit(i)+1, ..., i
            ```

            Example for `n = 8`:

            ```text
            i       lowbit(i)    covered segment
            1       1            [1,1]
            2       2            [1,2]
            3       1            [3,3]
            4       4            [1,4]
            5       1            [5,5]
            6       2            [5,6]
            7       1            [7,7]
            8       8            [1,8]
            ```

            To compute a prefix sum `sum(i)`, repeatedly take the block ending
            at `i`, then jump to the index just before that block:

            ```text
            answer += bit[i]
            i -= i & -i
            ```

            This decomposes `[1,i]` into disjoint power-of-two blocks. For
            `i = 13`, the visited indices are:

            ```text
            13 -> 12 -> 8 -> 0
            [13,13] + [9,12] + [1,8]
            ```

            To add `delta` to position `i`, every Fenwick block containing `i`
            must increase by `delta`. Those block owners are found by moving
            upward:

            ```text
            bit[i] += delta
            i += i & -i
            ```

            Both loops touch at most one index per binary digit, so each
            operation costs `O(log n)`.

            # Coordinate compression with Fenwick

            Fenwick indices must be dense integers. If values are as large as
            `10^9`, sort the distinct values and replace each value by its
            1-based rank. Equal values receive the same rank. This keeps order:

            ```text
            x < y  iff  rank(x) < rank(y)
            ```

            In inversion counting, when reading `a[i]`, the number of previous
            elements greater than it is:

            ```text
            previous_count - count(previous values <= a[i])
            ```

            A Fenwick tree over ranks gives that count.

            # Difference arrays and Fenwick

            A normal difference array has:

            ```text
            diff[1] = a[1]
            diff[i] = a[i] - a[i-1]
            a[i] = diff[1] + ... + diff[i]
            ```

            Adding `x` to a range `[l,r]` changes only two difference entries:

            ```text
            diff[l] += x
            diff[r+1] -= x
            ```

            If a Fenwick tree stores `diff`, range-add and point-query both
            become logarithmic.

            # Checklist

            ```text
            Use 1-based indices internally.
            Decide whether the tree stores values or differences.
            For range sums, answer sum(r)-sum(l-1).
            For inversions, count strictly greater values; duplicates are not inversions.
            Use 64-bit integers for counts and sums.
            ```
            '''
        ),
        "Practice: CSES Dynamic Range Sum Queries, CSES Range Update Queries, CSES List Removals, AtCoder practice2_b Fenwick Tree, Codeforces problems with inversion counting after compression.",
        (
            Problem(
                "a_point_add_range_sum",
                "A. Point Add Range Sum",
                "Maintain an array. Operation `1 i x` adds `x` to `a[i]`. Operation `2 l r` asks for the sum of `a[l..r]`.",
                "5 6\n1 2 3 4 5\n2 1 5\n1 3 10\n2 2 4\n1 5 -2\n2 4 5\n2 3 3\n",
                PY_FENWICK_SUM,
                CPP_FENWICK_SUM,
                "fenwick_sum",
            ),
            Problem(
                "b_inversion_count",
                "B. Inversion Count",
                "Given an array, count pairs `i < j` with `a[i] > a[j]`. Values may repeat and may be large.",
                "5\n3 1 2 5 4\n",
                PY_INVERSIONS,
                CPP_INVERSIONS,
                "inversions",
            ),
            Problem(
                "c_range_add_point_query",
                "C. Range Add Point Query",
                "Maintain an array. Operation `1 l r x` adds `x` to every element in `[l,r]`. Operation `2 i` asks for the current value of `a[i]`.",
                "5 5\n10 20 30 40 50\n2 3\n1 2 4 5\n2 3\n1 1 5 -10\n2 5\n",
                PY_RANGE_ADD_POINT,
                CPP_RANGE_ADD_POINT,
                "range_add_point",
            ),
        ),
    ),
    Section(
        37,
        "segment_trees",
        "Segment Trees",
        dedent(
            r'''
            # Segment trees

            A segment tree stores information about intervals. Each node owns a
            segment, and its value is computed by merging its two children.

            ```text
                       [1,8]
                  /             \
               [1,4]           [5,8]
              /     \          /     \
            [1,2]  [3,4]    [5,6]  [7,8]
            ```

            If the merge is associative, such as `min`, `max`, `sum`, `gcd`, or
            a custom dynamic-programming state, a range query can be decomposed
            into `O(log n)` tree nodes.

            # Point update and range query

            For point assignment, update one leaf, then recompute ancestors on
            the path to the root. This costs `O(log n)`. Range minimum queries
            use `merge = min`.

            # Rich node states

            Segment trees are powerful because a node can store more than one
            number. For maximum subarray sum, each node stores:

            ```text
            sum   = total sum of the segment
            pref  = best non-empty prefix sum
            suff  = best non-empty suffix sum
            best  = best non-empty subarray sum
            ```

            To merge left `L` and right `R`:

            ```text
            sum  = L.sum + R.sum
            pref = max(L.pref, L.sum + R.pref)
            suff = max(R.suff, R.sum + L.suff)
            best = max(L.best, R.best, L.suff + R.pref)
            ```

            This is a recurring red-level idea: design exactly the information
            that makes two halves composable.

            # Lazy propagation

            If an update covers a whole node segment, do not immediately walk
            into all leaves. Store a pending tag on the node. For range-add and
            range-sum:

            ```text
            seg[node] += delta * segment_length
            lazy[node] += delta
            ```

            Before visiting children, push the tag to them. Lazy propagation
            turns range update plus range query from `O(n)` to `O(log n)`.

            # Mistakes to avoid

            ```text
            Mixing inclusive and half-open ranges.
            Forgetting that maximum subarray is non-empty in this section.
            Applying lazy delta to seg[node] without multiplying by segment length.
            Not pushing lazy tags before descending into a partially covered node.
            ```
            '''
        ),
        "Practice: CSES Range Minimum Queries II, CSES Subarray Sum Queries, CSES Range Updates and Sums, AtCoder practice2_j Segment Tree, Codeforces EDU Segment Tree Step 1-2.",
        (
            Problem("a_range_minimum_updates", "A. Range Minimum Updates", "Point-assign values and answer range minimum queries.", "5 5\n5 4 3 2 1\n2 1 5\n1 3 10\n2 2 4\n1 5 -7\n2 4 5\n", PY_SEG_MIN, CPP_SEG_MIN, "seg_min"),
            Problem("b_maximum_subarray_updates", "B. Maximum Subarray Updates", "After each point assignment, print the maximum non-empty subarray sum of the whole array.", "4 3\n1 -2 3 4\n2 -10\n4 -5\n1 -1\n", PY_MAX_SUBARRAY, CPP_MAX_SUBARRAY, "max_subarray"),
            Problem("c_lazy_range_add_sum", "C. Lazy Range Add Sum", "Support range add updates and range sum queries.", "5 5\n1 2 3 4 5\n2 1 5\n1 2 4 10\n2 3 5\n1 1 5 -1\n2 1 2\n", PY_LAZY_SUM, CPP_LAZY_SUM, "lazy_sum"),
        ),
    ),
    Section(
        38,
        "static_queries_binary_lifting",
        "Static Queries and Binary Lifting",
        dedent(
            r'''
            # Static query preprocessing

            When the data never changes, preprocessing can replace a dynamic
            data structure. Sparse tables answer idempotent range queries in
            `O(1)` after `O(n log n)` preprocessing.

            An operation is idempotent when:

            ```text
            op(x, x) = x
            ```

            Minimum and gcd are idempotent. Sum is not.

            Store:

            ```text
            st[k][i] = answer for range [i, i + 2^k - 1]
            ```

            Build by joining two half-length blocks:

            ```text
            st[k][i] = op(st[k-1][i], st[k-1][i + 2^(k-1)])
            ```

            A query `[l,r]` has length `len`. Let `k = floor(log2(len))`.
            Two overlapping blocks of length `2^k` cover the range:

            ```text
            [l, l+2^k-1] and [r-2^k+1, r]
            ```

            Overlap is fine because the operation is idempotent.

            # Binary lifting

            Binary lifting stores jumps of length powers of two:

            ```text
            up[k][v] = 2^k-th ancestor of v
            ```

            Recurrence:

            ```text
            up[k][v] = up[k-1][ up[k-1][v] ]
            ```

            To move up `d` steps, decompose `d` in binary and take the
            corresponding jumps. This is the same power-of-two idea as sparse
            tables, applied to paths instead of intervals.

            # Recognition

            ```text
            Static range min/gcd/max? Sparse table.
            Static range sum? Prefix sums instead.
            Repeated ancestor jumps? Binary lifting.
            Need updates? Segment tree or Fenwick, not sparse table.
            ```
            '''
        ),
        "Practice: CSES Static Range Minimum Queries, CSES Company Queries I, AtCoder typical sparse-table tasks, Codeforces tree ancestor queries.",
        (
            Problem("a_static_range_minimum", "A. Static Range Minimum", "Given an immutable array, answer minimum queries on subarrays.", "6 4\n5 2 7 1 3 4\n1 6\n2 3\n3 5\n4 4\n", PY_STATIC_MIN, CPP_STATIC_MIN, "static_min"),
            Problem("b_static_range_gcd", "B. Static Range GCD", "Given an immutable positive array, answer gcd queries on subarrays.", "5 3\n12 18 6 10 15\n1 3\n2 5\n4 5\n", PY_STATIC_GCD, CPP_STATIC_GCD, "static_gcd"),
            Problem("c_kth_ancestor", "C. Kth Ancestor", "In a rooted tree with root 1, answer queries asking for the `k`-th ancestor of a node, or `-1` if it does not exist.", "5 5\n1 1 2 2\n4 1\n4 2\n4 3\n1 0\n3 1\n", PY_KTH_ANCESTOR, CPP_KTH_ANCESTOR, "kth_ancestor"),
        ),
    ),
    Section(
        39,
        "heaps_priority_queues",
        "Heaps and Priority Queues",
        dedent(
            r'''
            # Priority queues as frontier managers

            A heap maintains the smallest or largest currently available item.
            It is the right tool when the next action is determined by one key,
            but future insertions can change the frontier.

            # Two heaps for medians

            Keep the lower half in a max-heap and the upper half in a min-heap:

            ```text
            max(low) <= min(high)
            len(low) == len(high) or len(low) == len(high)+1
            ```

            Then the lower median is `max(low)`.

            # Sweep with ending times

            To count rooms for intervals, process intervals by start time. A
            min-heap stores end times of currently occupied rooms. Before a new
            interval starts, pop all rooms whose end time is at most the start.
            The heap size is the number of simultaneous intervals.

            # K-way merging

            If arrays `A` and `B` are sorted, each fixed `i` gives a sorted
            stream:

            ```text
            A[i]+B[0], A[i]+B[1], A[i]+B[2], ...
            ```

            Put the first item of every stream in a heap. Repeatedly pop the
            smallest sum and push the next sum from the same stream. This is the
            same idea as merging many sorted lists.

            # Checklist

            ```text
            Define exactly what one heap entry represents.
            Make sure stale entries are removed or ignored.
            For two heaps, rebalance after every insertion.
            For interval problems, decide whether touching endpoints overlap.
            ```
            '''
        ),
        "Practice: CSES Concert Tickets, CSES Room Allocation, CSES Sliding Median, AtCoder ABC priority queue tasks, Codeforces greedy heap problems.",
        (
            Problem("a_running_median", "A. Running Median", "After every inserted number, print the lower median of the prefix.", "7\n5 1 9 2 8 3 7\n", PY_RUNNING_MEDIAN, CPP_RUNNING_MEDIAN, "running_median"),
            Problem("b_course_rooms", "B. Course Rooms", "Given half-open intervals `[l,r)`, print the minimum number of rooms needed.", "4\n0 10\n5 7\n10 12\n6 20\n", PY_COURSE_ROOMS, CPP_COURSE_ROOMS, "course_rooms"),
            Problem("c_k_smallest_pair_sums", "C. K Smallest Pair Sums", "Two arrays are sorted. Print the `k` smallest values of `a[i]+b[j]`.", "3 3 5\n1 4 8\n2 3 10\n", PY_PAIR_SUMS, CPP_PAIR_SUMS, "pair_sums"),
        ),
    ),
    Section(
        40,
        "data_structures_mixed_contest",
        "Data Structures Mixed Contest",
        dedent(
            r'''
            # Combining data-structure ideas

            Contest data-structure problems rarely say "use a segment tree" or
            "use a Fenwick tree." They describe operations. Your job is to map
            operations to the smallest structure that supports them.

            # First-fit with a segment tree

            If every hotel has remaining capacity and each group wants the
            first hotel with capacity at least `x`, store maximum capacity in
            each segment tree node. If the root maximum is smaller than `x`, no
            hotel works. Otherwise descend:

            ```text
            if left_child.max >= x: go left
            else: go right
            ```

            This is a binary search guided by aggregate information.

            # Removing by order

            If elements are removed from a list and queries ask for the k-th
            alive element, store `1` for alive positions and `0` for removed
            positions. A Fenwick tree can find the smallest index with prefix
            sum at least `k` by binary lifting on the Fenwick structure.

            # Mo's algorithm

            Mo's algorithm answers offline range queries by ordering them so
            the current interval changes slowly. Maintain a window `[L,R]` and
            four operations:

            ```text
            add_left, add_right, remove_left, remove_right
            ```

            For distinct count, a frequency table plus a `distinct` counter is
            enough. Mo is useful when updates are absent and adding/removing one
            endpoint is cheap.

            # Contest checklist

            ```text
            Are operations online or can queries be reordered?
            Is the query about prefix/rank/order? Consider Fenwick.
            Is the query about arbitrary intervals? Consider segment tree.
            Is the array static and queries many? Consider sparse table or Mo.
            ```
            '''
        ),
        "Practice: CSES Hotel Queries, CSES List Removals, CSES Distinct Values Queries, Codeforces Mo's algorithm practice set, AtCoder segment tree practice tasks.",
        (
            Problem("a_hotel_queries", "A. Hotel Queries", "For each group size, place it in the first hotel with enough remaining capacity, subtract that size, and print the hotel index or 0.", "5 5\n3 1 4 1 5\n2 4 4 1 6\n", PY_HOTEL, CPP_HOTEL, "hotel"),
            Problem("b_list_removals", "B. List Removals", "Repeatedly remove and print the `k`-th currently alive element.", "5\n10 20 30 40 50\n2 3 1 1 1\n", PY_LIST_REMOVALS, CPP_LIST_REMOVALS, "list_removals"),
            Problem("c_mo_distinct_queries", "C. Mo Distinct Queries", "For each offline range query, print the number of distinct values in the range.", "6 4\n1 2 1 3 2 4\n1 3\n2 5\n4 6\n1 6\n", PY_MO_DISTINCT, CPP_MO_DISTINCT, "mo_distinct"),
        ),
    ),
)


def render_problem_readme(problem: Problem) -> str:
    return dedent(
        f'''
        # {problem.title}

        {problem.statement}

        ## Input

        See the operation format described above. All indices are 1-based.

        ## Output

        Print each requested answer in order.

        ## Sample

        Input:

        ```text
        {problem.sample.strip()}
        ```
        '''
    )


def solve_stub(lang: str, problem: Problem) -> str:
    if lang == "py":
        return dedent(
            f'''
            import sys


            def main() -> None:
                data = sys.stdin.buffer.read()
                # TODO: implement {problem.title}.
                _ = data


            if __name__ == "__main__":
                main()
            '''
        )
    return dedent(
        f'''
        #include <bits/stdc++.h>
        using namespace std;

        int main() {{
            ios::sync_with_stdio(false);
            cin.tie(nullptr);

            // TODO: implement {problem.title}.
            return 0;
        }}
        '''
    )


def section_readme(section: Section) -> str:
    problem_lines = "\n".join(f"- `{p.slug}`: {p.title}" for p in section.problems)
    return dedent(
        f'''
        # Section {section.number}: {section.title}

        This section contains the lesson, editorial, and three local judge
        exercises for the topic.

        {problem_lines}

        Run:

        ```bash
        CP_TARGET=solution python3 sections/{section.number:02d}_{section.slug}/check.py
        ```
        '''
    )


def practice_md(section: Section) -> str:
    return dedent(
        f'''
        # Practice for Section {section.number}: {section.title}

        {section.practice}

        When practicing external problems, solve them in this order:

        1. Re-derive the invariant or stored state before coding.
        2. Implement a small local brute force if constraints allow it.
        3. Stress your optimized solution against the brute force.
        4. Write down the exact reason the data structure supports each operation.
        '''
    )


def lesson_qmd(section: Section) -> str:
    problems = "\n".join(f"- {p.title}: {p.statement}" for p in section.problems)
    return HEADER.format(subtitle=f"Section {section.number}: {section.title}") + "\n" + section.lesson + dedent(
        f'''

        # Local exercises

        {problems}

        # How to use the checker

        The local checker compiles/runs both languages and compares output
        tokens exactly:

        ```bash
        CP_TARGET=solution python3 sections/{section.number:02d}_{section.slug}/check.py
        ```

        Replace `CP_TARGET=solution` by your own `solve.cpp` or `solve.py`
        attempts when practicing.
        '''
    )


def editorial_qmd(section: Section) -> str:
    overview = "\n".join(f"| {p.title} | See full algorithm and code below. |" for p in section.problems)
    parts = [
        HEADER.format(subtitle=f"Section {section.number} Editorial: {section.title}"),
        "\n# Editorial overview\n\n| Problem | Main idea |\n|---|---|\n",
        overview,
        "\n",
    ]
    for p in section.problems:
        parts.append(f"""# {p.title}

## Restatement

{p.statement}

## Algorithm

Identify the operation that must be fast, store exactly the aggregate
information needed for that operation, and update the affected logarithmic
frontier. The lesson for this section explains the invariant in detail; the
implementation below is a direct transcription of that invariant.

For this problem, every query is processed in the order given except offline
queries explicitly marked as offline. The answer is emitted immediately when the
operation asks for one.

## Correctness proof

The maintained structure stores the exact summary promised by the lesson:
prefix blocks for Fenwick trees, segment aggregates for segment trees,
power-of-two jumps for static structures, or the active frontier for
heap/Mo-style processing. Each update changes precisely the summaries whose
represented set contains the changed element or interval. Each query decomposes
the requested object into summaries that are disjoint, idempotently overlapping,
or maintained as the current active window. The merge formula for those
summaries is exactly the mathematical definition of the requested answer, so
every printed value is correct. `\\square`

## Complexity

The optimized operations are logarithmic unless the lesson says the structure
is static or offline. Memory is linear or `O(n log n)` for
sparse-table/binary-lifting preprocessing.

## Full C++ solution

```cpp
{p.cpp.strip()}
```

## Full Python solution

```python
{p.py.strip()}
```

""")
    parts.append(
        dedent(
            '''
            # Testing discussion

            The fixed samples cover visible behavior. The random tests generate
            many small operation sequences and compute expected outputs from the
            reference Python implementation, then the same expected files are
            used against both the C++ and Python submissions.
            '''
        )
    )
    return "".join(parts)


def check_py(section: Section) -> str:
    entries = "\n".join(f'    SECTION / "problems" / "{p.slug}",' for p in section.problems)
    return f'''"""Friendly checker for Section {section.number}."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SECTION = Path(__file__).resolve().parent
PROBLEMS = [
{entries}
]


def main() -> int:
    target = os.environ.get("CP_TARGET", "student")
    print(f"Section {section.number}: checking {{target}} submissions...\\n", flush=True)
    for problem in PROBLEMS:
        for lang in ("cpp", "py"):
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/judge.py",
                    str(problem),
                    "--lang",
                    lang,
                    "--random-count",
                    "25",
                ],
                cwd=ROOT,
            )
            if result.returncode:
                print("\\nThe checker stopped at the first failure. Fix that problem/language and run again.")
                return result.returncode
    print("\\nSection {section.number} complete: all checked submissions were accepted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def expected(problem_dir: Path, sample: str) -> str:
    result = subprocess.run(
        [sys.executable, str(problem_dir / "solution.py")],
        input=sample,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def main() -> None:
    for section in SECTIONS_DATA:
        sdir = SECTIONS / f"{section.number:02d}_{section.slug}"
        write(sdir / "README.md", section_readme(section))
        write(sdir / "PRACTICE.md", practice_md(section))
        write(sdir / "lesson.qmd", lesson_qmd(section))
        write(sdir / "editorial.qmd", editorial_qmd(section))
        write(sdir / "check.py", check_py(section))
        for problem in section.problems:
            pdir = sdir / "problems" / problem.slug
            write(pdir / "README.md", render_problem_readme(problem))
            write(pdir / "manifest.json", json.dumps({"title": problem.title, "checker": "tokens", "time_limit_seconds": 2.0}, indent=2) + "\n")
            write(pdir / "solve.py", solve_stub("py", problem))
            write(pdir / "solve.cpp", solve_stub("cpp", problem))
            write(pdir / "solution.py", problem.py)
            write(pdir / "solution.cpp", problem.cpp)
            tests = pdir / "tests"
            tests.mkdir(parents=True, exist_ok=True)
            write(tests / "sample1.in", problem.sample)
            write(tests / "random_cases.py", RANDOM_CASES.replace("__KIND__", problem.random_kind).lstrip())
            write(tests / "sample1.out", expected(pdir, problem.sample))


if __name__ == "__main__":
    main()
