"""Independent tiny-instance generators for Sections 67--69."""

from __future__ import annotations
import argparse, collections, itertools, math, random
from pathlib import Path

MOD = 998_244_353


def tree(rng, n, weighted=False):
    edges = []
    for v in range(1, n):
        edges.append((rng.randrange(v), v, rng.randint(1, 8) if weighted else 1))
    return edges


def graph(n, edges):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    return g


def path(g, start, target):
    parent = [-1] * len(g)
    parent[start] = start
    q = collections.deque([start])
    while q:
        u = q.popleft()
        for v, _ in g[u]:
            if parent[v] < 0:
                parent[v] = u
                q.append(v)
    result = []
    u = target
    while u != start:
        result.append(u)
        u = parent[u]
    return [start] + result[::-1]


def distances(g, start):
    d = [-1] * len(g)
    d[start] = 0
    stack = [start]
    for u in stack:
        for v, w in g[u]:
            if d[v] < 0:
                d[v] = d[u] + w
                stack.append(v)
    return d


def components(n, active):
    g = [[] for _ in range(n)]
    for u, v in active:
        g[u].append(v)
        g[v].append(u)
    return g


def connected(g, u, v):
    seen = {u}
    stack = [u]
    for x in stack:
        for y in g[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return v in seen, len(seen)


def generate(slug, rng):
    if slug == "a_branching_multiset":
        m = rng.randint(2, 15)
        versions = [[]]
        ops = []
        out = []
        for _ in range(rng.randint(8, 35)):
            if rng.random() < 0.65 or all(not v for v in versions):
                v = rng.randrange(len(versions))
                a = versions[v][:]
                if a and rng.random() < 0.3:
                    x = rng.choice(a)
                    a.remove(x)
                    ops.append(f"E {v} {x}")
                else:
                    x = rng.randint(1, m)
                    a.append(x)
                    ops.append(f"I {v} {x}")
                versions.append(a)
            else:
                choices = [i for i, v in enumerate(versions) if v]
                v = rng.choice(choices)
                if rng.random() < 0.5:
                    k = rng.randint(1, len(versions[v]))
                    ops.append(f"K {v} {k}")
                    out.append(str(sorted(versions[v])[k - 1]))
                else:
                    x = rng.randint(1, m)
                    ops.append(f"C {v} {x}")
                    out.append(str(sum(y <= x for y in versions[v])))
        return f"{m} {len(ops)}\n" + "\n".join(ops) + "\n", "\n".join(out) + (
            "\n" if out else ""
        )
    if slug == "b_versioned_range_add":
        n = rng.randint(1, 10)
        initial = [rng.randint(-5, 5) for _ in range(n)]
        versions = [initial]
        ops = []
        out = []
        for _ in range(rng.randint(8, 30)):
            v = rng.randrange(len(versions))
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            if rng.random() < 0.6:
                x = rng.randint(-5, 5)
                a = versions[v][:]
                for i in range(l - 1, r):
                    a[i] += x
                versions.append(a)
                ops.append(f"A {v} {l} {r} {x}")
            else:
                ops.append(f"Q {v} {l} {r}")
                out.append(str(sum(versions[v][l - 1 : r])))
        return f"{n} {len(ops)}\n" + " ".join(map(str, initial)) + "\n" + "\n".join(
            ops
        ) + "\n", "\n".join(out) + ("\n" if out else "")
    if slug in {"c_dynamic_connectivity", "b_seasonal_component_size"}:
        n = rng.randint(2, 10)
        active = set()
        ops = []
        out = []
        for _ in range(rng.randint(10, 40)):
            all_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
            roll = rng.random()
            if roll < 0.35 and len(active) < len(all_edges):
                e = rng.choice([e for e in all_edges if e not in active])
                active.add(e)
                ops.append(f"+ {e[0]+1} {e[1]+1}")
            elif roll < 0.55 and active:
                e = rng.choice(tuple(active))
                active.remove(e)
                ops.append(f"- {e[0]+1} {e[1]+1}")
            else:
                g = components(n, active)
                u = rng.randrange(n)
                if slug == "c_dynamic_connectivity":
                    v = rng.randrange(n)
                    ops.append(f"? {u+1} {v+1}")
                    out.append("YES" if connected(g, u, v)[0] else "NO")
                else:
                    ops.append(f"S {u+1}")
                    out.append(str(connected(g, u, u)[1]))
        return f"{n} {len(ops)}\n" + "\n".join(ops) + "\n", "\n".join(out) + "\n"
    if slug in {"a_path_affine_composition", "c_route_matrices"}:
        n = rng.randint(1, 10)
        edges = tree(rng, n)
        g = graph(n, edges)
        ops = []
        out = []
        if slug == "a_path_affine_composition":
            values = [(rng.randrange(8), rng.randrange(8)) for _ in range(n)]
            initial = values[:]
            for _ in range(rng.randint(8, 30)):
                u = rng.randrange(n)
                if rng.random() < 0.35:
                    values[u] = (rng.randrange(8), rng.randrange(8))
                    ops.append(f"U {u+1} {values[u][0]} {values[u][1]}")
                else:
                    v = rng.randrange(n)
                    x = rng.randrange(20)
                    y = x
                    for node in path(g, u, v):
                        a, b = values[node]
                        y = (a * y + b) % MOD
                    ops.append(f"Q {u+1} {v+1} {x}")
                    out.append(str(y))
            head = (
                f"{n} {len(ops)}\n" + "\n".join(f"{a} {b}" for a, b in initial) + "\n"
            )
        else:
            values = [tuple(rng.randrange(8) for _ in range(4)) for _ in range(n)]
            initial = values[:]

            def mul(a, b):
                return (
                    (a[0] * b[0] + a[1] * b[2]) % MOD,
                    (a[0] * b[1] + a[1] * b[3]) % MOD,
                    (a[2] * b[0] + a[3] * b[2]) % MOD,
                    (a[2] * b[1] + a[3] * b[3]) % MOD,
                )

            for _ in range(rng.randint(8, 30)):
                u = rng.randrange(n)
                if rng.random() < 0.35:
                    values[u] = tuple(rng.randrange(8) for _ in range(4))
                    ops.append(f"U {u+1} " + " ".join(map(str, values[u])))
                else:
                    v = rng.randrange(n)
                    answer = (1, 0, 0, 1)
                    for node in path(g, u, v):
                        answer = mul(answer, values[node])
                    ops.append(f"Q {u+1} {v+1}")
                    out.append(" ".join(map(str, answer)))
            head = (
                f"{n} {len(ops)}\n"
                + "\n".join(" ".join(map(str, m)) for m in initial)
                + "\n"
            )
        edge_text = "\n".join(f"{u+1} {v+1}" for u, v, _ in edges)
        return head + edge_text + ("\n" if edges else "") + "\n".join(
            ops
        ) + "\n", "\n".join(out) + ("\n" if out else "")
    if slug in {"b_toggle_nearest_beacon", "d_beacon_distance_sum"}:
        n = rng.randint(1, 12)
        edges = tree(rng, n)
        g = graph(n, edges)
        all_dist = [distances(g, u) for u in range(n)]
        active = set()
        ops = []
        out = []
        for _ in range(rng.randint(8, 35)):
            u = rng.randrange(n)
            if rng.random() < 0.55:
                active.symmetric_difference_update({u})
                ops.append(f"T {u+1}")
            else:
                ops.append(f"Q {u+1}")
                if slug == "b_toggle_nearest_beacon":
                    out.append(str(min((all_dist[u][v] for v in active), default=-1)))
                else:
                    out.append(str(sum(all_dist[u][v] for v in active)))
        text = (
            f"{n} {len(ops)}\n"
            + "\n".join(f"{u+1} {v+1}" for u, v, _ in edges)
            + ("\n" if edges else "")
            + "\n".join(ops)
            + "\n"
        )
        return text, "\n".join(out) + ("\n" if out else "")
    if slug in {"c_marked_pair_distances", "e_weighted_marked_pairs"}:
        n = rng.randint(2, 12)
        edges = tree(rng, n, True)
        g = graph(n, edges)
        dist = [distances(g, u) for u in range(n)]
        queries = []
        out = []
        for _ in range(rng.randint(2, 10)):
            nodes = rng.sample(range(n), rng.randint(1, n))
            if slug == "c_marked_pair_distances":
                queries.append(
                    str(len(nodes)) + " " + " ".join(str(x + 1) for x in nodes)
                )
                out.append(
                    str(
                        sum(
                            dist[u][v]
                            for i, u in enumerate(nodes)
                            for v in nodes[i + 1 :]
                        )
                    )
                )
            else:
                weights = [rng.randint(1, 5) for _ in nodes]
                queries.append(
                    str(len(nodes))
                    + " "
                    + " ".join(f"{u+1} {w}" for u, w in zip(nodes, weights))
                )
                out.append(
                    str(
                        sum(
                            weights[i] * weights[j] * dist[nodes[i]][nodes[j]]
                            for i in range(len(nodes))
                            for j in range(i + 1, len(nodes))
                        )
                    )
                )
        text = (
            f"{n} {len(queries)}\n"
            + "\n".join(f"{u+1} {v+1} {w}" for u, v, w in edges)
            + "\n"
            + "\n".join(queries)
            + "\n"
        )
        return text, "\n".join(out) + "\n"
    if slug in {"d_subtree_mode_sum", "f_subtree_frequency_profile"}:
        n = rng.randint(1, 14)
        edges = tree(rng, n)
        g = graph(n, edges)
        colors = [rng.randint(1, 6) for _ in range(n)]
        parent = [-1] * n
        order = [0]
        for u in order:
            for v, _ in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        children = [[] for _ in range(n)]
        for v in range(1, n):
            children[parent[v]].append(v)
        answers = [None] * n
        for u in reversed(order):
            nodes = [u]
            for x in nodes:
                nodes.extend(children[x])
            counter = collections.Counter(colors[x] for x in nodes)
            best = max(counter.values())
            modes = [c for c, v in counter.items() if v == best]
            answers[u] = (
                str(sum(modes))
                if slug == "d_subtree_mode_sum"
                else f"{best} {len(modes)}"
            )
        text = (
            f"{n}\n"
            + " ".join(map(str, colors))
            + "\n"
            + "\n".join(f"{u+1} {v+1}" for u, v, _ in edges)
            + ("\n" if edges else "")
        )
        return text, "\n".join(answers) + "\n"
    if slug == "a_snapshot_rank":
        maximum = rng.randint(3, 15)
        seq = [[]]
        ops = []
        out = []
        for _ in range(rng.randint(10, 35)):
            if rng.random() < 0.65 or len(seq) == 1:
                v = rng.randrange(len(seq))
                x = rng.randint(1, maximum)
                seq.append(seq[v] + [x])
                ops.append(f"A {v} {x}")
            else:
                choices = [i for i, a in enumerate(seq) if a]
                v = rng.choice(choices)
                l = rng.randint(1, len(seq[v]))
                r = rng.randint(l, len(seq[v]))
                k = rng.randint(1, r - l + 1)
                ops.append(f"Q {v} {l} {r} {k}")
                out.append(str(sorted(seq[v][l - 1 : r])[k - 1]))
        return f"{maximum} {len(ops)}\n" + "\n".join(ops) + "\n", "\n".join(out) + (
            "\n" if out else ""
        )
    raise ValueError(slug)


def main(slug):
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        inp, out = generate(slug, rng)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(inp)
        stem.with_suffix(".out").write_text(out)
