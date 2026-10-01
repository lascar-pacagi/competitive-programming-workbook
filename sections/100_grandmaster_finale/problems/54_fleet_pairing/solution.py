import sys

# Maximum-weight matching in a general graph: Edmonds' primal--dual blossom
# algorithm in the O(n^3) formulation of Galil, following the structure of
# van Rantwijk's reference implementation.  Vertex duals start at max weight;
# every stage grows alternating trees with tight edges, shrinks odd cycles into
# blossoms, and otherwise changes duals by the smallest of four slack bounds.


def max_weight_matching(nvertex, edges):
    nedge = len(edges)
    if nedge == 0:
        return [-1] * nvertex
    maxweight = max(0, max(w for _, _, w in edges))
    endpoint = [edges[p >> 1][p & 1] for p in range(2 * nedge)]
    neighbend = [[] for _ in range(nvertex)]
    for k, (i, j, _) in enumerate(edges):
        neighbend[i].append(2 * k + 1)
        neighbend[j].append(2 * k)
    mate = [-1] * nvertex
    label = [0] * (2 * nvertex)
    labelend = [-1] * (2 * nvertex)
    inblossom = list(range(nvertex))
    blossomparent = [-1] * (2 * nvertex)
    blossomchilds = [None] * (2 * nvertex)
    blossombase = list(range(nvertex)) + [-1] * nvertex
    blossomendps = [None] * (2 * nvertex)
    bestedge = [-1] * (2 * nvertex)
    blossombestedges = [None] * (2 * nvertex)
    unusedblossoms = list(range(nvertex, 2 * nvertex))
    dualvar = [maxweight] * nvertex + [0] * nvertex
    allowedge = [False] * nedge
    queue = []

    def slack(k):
        i, j, wt = edges[k]
        return dualvar[i] + dualvar[j] - 2 * wt

    def leaves(b):
        if b < nvertex:
            return [b]
        out = []
        stack = [b]
        while stack:
            t = stack.pop()
            if t < nvertex:
                out.append(t)
            else:
                stack.extend(blossomchilds[t])
        return out

    def assign_label(w, t, p):
        while True:
            b = inblossom[w]
            label[w] = label[b] = t
            labelend[w] = labelend[b] = p
            bestedge[w] = bestedge[b] = -1
            if t == 1:
                queue.extend(leaves(b))
                return
            base = blossombase[b]
            w = endpoint[mate[base]]
            t = 1
            p = mate[base] ^ 1

    def scan_blossom(v, w):
        path = []
        base = -1
        while v != -1 or w != -1:
            b = inblossom[v]
            if label[b] & 4:
                base = blossombase[b]
                break
            path.append(b)
            label[b] = 5
            if labelend[b] == -1:
                v = -1
            else:
                v = endpoint[labelend[b]]
                b = inblossom[v]
                v = endpoint[labelend[b]]
            if w != -1:
                v, w = w, v
        for b in path:
            label[b] = 1
        return base

    def add_blossom(base, k):
        v, w, _ = edges[k]
        bb = inblossom[base]
        bv = inblossom[v]
        bw = inblossom[w]
        b = unusedblossoms.pop()
        blossombase[b] = base
        blossomparent[b] = -1
        blossomparent[bb] = b
        path = []
        endps = []
        while bv != bb:
            blossomparent[bv] = b
            path.append(bv)
            endps.append(labelend[bv])
            v = endpoint[labelend[bv]]
            bv = inblossom[v]
        path.append(bb)
        path.reverse()
        endps.reverse()
        endps.append(2 * k)
        while bw != bb:
            blossomparent[bw] = b
            path.append(bw)
            endps.append(labelend[bw] ^ 1)
            w = endpoint[labelend[bw]]
            bw = inblossom[w]
        blossomchilds[b] = path
        blossomendps[b] = endps
        label[b] = 1
        labelend[b] = labelend[bb]
        dualvar[b] = 0
        for v in leaves(b):
            if label[inblossom[v]] == 2:
                queue.append(v)
            inblossom[v] = b
        bestedgeto = [-1] * (2 * nvertex)
        for bv in path:
            if blossombestedges[bv] is None:
                nblists = [[p >> 1 for p in neighbend[v]] for v in leaves(bv)]
            else:
                nblists = [blossombestedges[bv]]
            for nblist in nblists:
                for k in nblist:
                    i, j, _ = edges[k]
                    if inblossom[j] == b:
                        i, j = j, i
                    bj = inblossom[j]
                    if bj != b and label[bj] == 1 and (bestedgeto[bj] == -1 or slack(k) < slack(bestedgeto[bj])):
                        bestedgeto[bj] = k
            blossombestedges[bv] = None
            bestedge[bv] = -1
        blossombestedges[b] = [k for k in bestedgeto if k != -1]
        bestedge[b] = -1
        for k in blossombestedges[b]:
            if bestedge[b] == -1 or slack(k) < slack(bestedge[b]):
                bestedge[b] = k

    def expand_blossom(b, endstage):
        for s in blossomchilds[b]:
            blossomparent[s] = -1
            if s < nvertex:
                inblossom[s] = s
            elif endstage and dualvar[s] == 0:
                expand_blossom(s, endstage)
            else:
                for v in leaves(s):
                    inblossom[v] = s
        if not endstage and label[b] == 2:
            childs = blossomchilds[b]
            endps = blossomendps[b]
            entrychild = inblossom[endpoint[labelend[b] ^ 1]]
            j = childs.index(entrychild)
            if j & 1:
                j -= len(childs)
                jstep = 1
                endptrick = 0
            else:
                jstep = -1
                endptrick = 1
            p = labelend[b]
            while j != 0:
                label[endpoint[p ^ 1]] = 0
                label[endpoint[endps[j - endptrick] ^ endptrick ^ 1]] = 0
                assign_label(endpoint[p ^ 1], 2, p)
                allowedge[endps[j - endptrick] >> 1] = True
                j += jstep
                p = endps[j - endptrick] ^ endptrick
                allowedge[p >> 1] = True
                j += jstep
            bv = childs[j]
            label[endpoint[p ^ 1]] = label[bv] = 2
            labelend[endpoint[p ^ 1]] = labelend[bv] = p
            bestedge[bv] = -1
            j += jstep
            while childs[j] != entrychild:
                bv = childs[j]
                if label[bv] == 1:
                    j += jstep
                    continue
                found = -1
                for v in leaves(bv):
                    if label[v] != 0:
                        found = v
                        break
                if found >= 0:
                    label[found] = 0
                    label[endpoint[mate[blossombase[bv]]]] = 0
                    assign_label(found, 2, labelend[found])
                j += jstep
        label[b] = labelend[b] = -1
        blossomchilds[b] = blossomendps[b] = None
        blossombase[b] = -1
        blossombestedges[b] = None
        bestedge[b] = -1
        unusedblossoms.append(b)

    def augment_blossom(b, v):
        t = v
        while blossomparent[t] != b:
            t = blossomparent[t]
        if t >= nvertex:
            augment_blossom(t, v)
        i = j = blossomchilds[b].index(t)
        if i & 1:
            j -= len(blossomchilds[b])
            jstep = 1
            endptrick = 0
        else:
            jstep = -1
            endptrick = 1
        while j != 0:
            j += jstep
            t = blossomchilds[b][j]
            p = blossomendps[b][j - endptrick] ^ endptrick
            if t >= nvertex:
                augment_blossom(t, endpoint[p])
            j += jstep
            t = blossomchilds[b][j]
            if t >= nvertex:
                augment_blossom(t, endpoint[p ^ 1])
            mate[endpoint[p]] = p ^ 1
            mate[endpoint[p ^ 1]] = p
        blossomchilds[b] = blossomchilds[b][i:] + blossomchilds[b][:i]
        blossomendps[b] = blossomendps[b][i:] + blossomendps[b][:i]
        blossombase[b] = blossombase[blossomchilds[b][0]]

    def augment_matching(k):
        v, w, _ = edges[k]
        for s, p in ((v, 2 * k + 1), (w, 2 * k)):
            while True:
                bs = inblossom[s]
                if bs >= nvertex:
                    augment_blossom(bs, s)
                mate[s] = p
                if labelend[bs] == -1:
                    break
                t = endpoint[labelend[bs]]
                bt = inblossom[t]
                s = endpoint[labelend[bt]]
                j = endpoint[labelend[bt] ^ 1]
                if bt >= nvertex:
                    augment_blossom(bt, j)
                mate[j] = labelend[bt]
                p = labelend[bt] ^ 1

    for _ in range(nvertex):
        label[:] = [0] * (2 * nvertex)
        bestedge[:] = [-1] * (2 * nvertex)
        blossombestedges[nvertex:] = [None] * nvertex
        allowedge[:] = [False] * nedge
        queue[:] = []
        for v in range(nvertex):
            if mate[v] == -1 and label[inblossom[v]] == 0:
                assign_label(v, 1, -1)
        augmented = False
        while True:
            while queue and not augmented:
                v = queue.pop()
                for p in neighbend[v]:
                    k = p >> 1
                    w = endpoint[p]
                    if inblossom[v] == inblossom[w]:
                        continue
                    if not allowedge[k]:
                        kslack = slack(k)
                        if kslack <= 0:
                            allowedge[k] = True
                    if allowedge[k]:
                        if label[inblossom[w]] == 0:
                            assign_label(w, 2, p ^ 1)
                        elif label[inblossom[w]] == 1:
                            base = scan_blossom(v, w)
                            if base >= 0:
                                add_blossom(base, k)
                            else:
                                augment_matching(k)
                                augmented = True
                                break
                        elif label[w] == 0:
                            label[w] = 2
                            labelend[w] = p ^ 1
                    elif label[inblossom[w]] == 1:
                        b = inblossom[v]
                        if bestedge[b] == -1 or kslack < slack(bestedge[b]):
                            bestedge[b] = k
                    elif label[w] == 0:
                        if bestedge[w] == -1 or kslack < slack(bestedge[w]):
                            bestedge[w] = k
            if augmented:
                break
            deltatype = 1
            delta = min(dualvar[:nvertex])
            deltaedge = deltablossom = -1
            for v in range(nvertex):
                if label[inblossom[v]] == 0 and bestedge[v] != -1:
                    d = slack(bestedge[v])
                    if d < delta:
                        delta = d
                        deltatype = 2
                        deltaedge = bestedge[v]
            for b in range(2 * nvertex):
                if blossomparent[b] == -1 and label[b] == 1 and bestedge[b] != -1:
                    d = slack(bestedge[b]) >> 1
                    if d < delta:
                        delta = d
                        deltatype = 3
                        deltaedge = bestedge[b]
            for b in range(nvertex, 2 * nvertex):
                if blossombase[b] >= 0 and blossomparent[b] == -1 and label[b] == 2 and dualvar[b] < delta:
                    delta = dualvar[b]
                    deltatype = 4
                    deltablossom = b
            for v in range(nvertex):
                lb = label[inblossom[v]]
                if lb == 1:
                    dualvar[v] -= delta
                elif lb == 2:
                    dualvar[v] += delta
            for b in range(nvertex, 2 * nvertex):
                if blossombase[b] >= 0 and blossomparent[b] == -1:
                    if label[b] == 1:
                        dualvar[b] += delta
                    elif label[b] == 2:
                        dualvar[b] -= delta
            if deltatype == 1:
                break
            if deltatype == 2:
                allowedge[deltaedge] = True
                i, j, _ = edges[deltaedge]
                if label[inblossom[i]] == 0:
                    i, j = j, i
                queue.append(i)
            elif deltatype == 3:
                allowedge[deltaedge] = True
                i, j, _ = edges[deltaedge]
                queue.append(i)
            else:
                expand_blossom(deltablossom, False)
        if not augmented:
            break
        for b in range(nvertex, 2 * nvertex):
            if blossomparent[b] == -1 and blossombase[b] >= 0 and label[b] == 1 and dualvar[b] == 0:
                expand_blossom(b, True)
    return [endpoint[m] if m >= 0 else -1 for m in mate]


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    best = {}
    for i in range(m):
        u = int(data[2 + 3 * i]) - 1
        v = int(data[3 + 3 * i]) - 1
        w = int(data[4 + 3 * i])
        if u != v:
            key = (u, v) if u < v else (v, u)
            if best.get(key, 0) < w:
                best[key] = w
    # Parallel offers collapse to the best one; doubled weights keep every
    # dual update integral.
    edges = [(u, v, 2 * w) for (u, v), w in best.items()]
    mate = max_weight_matching(n, edges)
    total = 0
    for v in range(n):
        if mate[v] > v:
            total += best[(v, mate[v])]
    print(total)


if __name__ == "__main__":
    main()
