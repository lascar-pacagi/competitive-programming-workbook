#include <bits/stdc++.h>
using namespace std;

// Maximum-weight matching in a general graph: Edmonds' primal--dual blossom
// algorithm in Galil's O(n^3) formulation (same structure as the Python
// reference).  Vertex duals start at the maximum weight; each stage grows
// alternating trees on tight edges, shrinks odd cycles into blossoms, and
// otherwise moves the duals by the smallest of four slack bounds.

typedef long long ll;

struct Matcher {
    int nv, ne;
    vector<array<ll, 3>> edges;  // u, v, doubled weight
    vector<int> endpoint, mate, label, labelend, inblossom, blossomparent, blossombase, bestedge,
        unusedblossoms, queue;
    vector<vector<int>> neighbend, blossomchilds, blossomendps, blossombestedges;
    vector<char> hasBestList, allowedge;
    vector<ll> dualvar;

    ll slack(int k) { return dualvar[edges[k][0]] + dualvar[edges[k][1]] - 2 * edges[k][2]; }

    void leaves(int b, vector<int>& out) {
        if (b < nv) {
            out.push_back(b);
            return;
        }
        for (int t : blossomchilds[b]) leaves(t, out);
    }

    void assignLabel(int w, int t, int p) {
        while (true) {
            int b = inblossom[w];
            label[w] = label[b] = t;
            labelend[w] = labelend[b] = p;
            bestedge[w] = bestedge[b] = -1;
            if (t == 1) {
                leaves(b, queue);
                return;
            }
            int base = blossombase[b];
            w = endpoint[mate[base]];
            t = 1;
            p = mate[base] ^ 1;
        }
    }

    int scanBlossom(int v, int w) {
        vector<int> path;
        int base = -1;
        while (v != -1 || w != -1) {
            int b = inblossom[v];
            if (label[b] & 4) {
                base = blossombase[b];
                break;
            }
            path.push_back(b);
            label[b] = 5;
            if (labelend[b] == -1) {
                v = -1;
            } else {
                v = endpoint[labelend[b]];
                b = inblossom[v];
                v = endpoint[labelend[b]];
            }
            if (w != -1) swap(v, w);
        }
        for (int b : path) label[b] = 1;
        return base;
    }

    void addBlossom(int base, int k) {
        int v = edges[k][0], w = edges[k][1];
        int bb = inblossom[base], bv = inblossom[v], bw = inblossom[w];
        int b = unusedblossoms.back();
        unusedblossoms.pop_back();
        blossombase[b] = base;
        blossomparent[b] = -1;
        blossomparent[bb] = b;
        vector<int> path, endps;
        while (bv != bb) {
            blossomparent[bv] = b;
            path.push_back(bv);
            endps.push_back(labelend[bv]);
            v = endpoint[labelend[bv]];
            bv = inblossom[v];
        }
        path.push_back(bb);
        reverse(path.begin(), path.end());
        reverse(endps.begin(), endps.end());
        endps.push_back(2 * k);
        while (bw != bb) {
            blossomparent[bw] = b;
            path.push_back(bw);
            endps.push_back(labelend[bw] ^ 1);
            w = endpoint[labelend[bw]];
            bw = inblossom[w];
        }
        blossomchilds[b] = path;
        blossomendps[b] = endps;
        label[b] = 1;
        labelend[b] = labelend[bb];
        dualvar[b] = 0;
        vector<int> lv;
        leaves(b, lv);
        for (int x : lv) {
            if (label[inblossom[x]] == 2) queue.push_back(x);
            inblossom[x] = b;
        }
        vector<int> bestedgeto(2 * nv, -1);
        for (int sub : path) {
            vector<int> candidates;
            if (!hasBestList[sub]) {
                vector<int> sl;
                leaves(sub, sl);
                for (int x : sl)
                    for (int p : neighbend[x]) candidates.push_back(p >> 1);
            } else {
                candidates = blossombestedges[sub];
            }
            for (int kk : candidates) {
                int i = edges[kk][0], j = edges[kk][1];
                if (inblossom[j] == b) swap(i, j);
                int bj = inblossom[j];
                if (bj != b && label[bj] == 1 && (bestedgeto[bj] == -1 || slack(kk) < slack(bestedgeto[bj])))
                    bestedgeto[bj] = kk;
            }
            hasBestList[sub] = 0;
            blossombestedges[sub].clear();
            bestedge[sub] = -1;
        }
        blossombestedges[b].clear();
        for (int kk : bestedgeto)
            if (kk != -1) blossombestedges[b].push_back(kk);
        hasBestList[b] = 1;
        bestedge[b] = -1;
        for (int kk : blossombestedges[b])
            if (bestedge[b] == -1 || slack(kk) < slack(bestedge[b])) bestedge[b] = kk;
    }

    void expandBlossom(int b, bool endstage) {
        for (int s : blossomchilds[b]) {
            blossomparent[s] = -1;
            if (s < nv) {
                inblossom[s] = s;
            } else if (endstage && dualvar[s] == 0) {
                expandBlossom(s, endstage);
            } else {
                vector<int> lv;
                leaves(s, lv);
                for (int x : lv) inblossom[x] = s;
            }
        }
        if (!endstage && label[b] == 2) {
            vector<int>& childs = blossomchilds[b];
            vector<int>& endps = blossomendps[b];
            int L = childs.size();
            auto at = [&](vector<int>& vec, int idx) -> int& { return vec[((idx % L) + L) % L]; };
            int entrychild = inblossom[endpoint[labelend[b] ^ 1]];
            int j = find(childs.begin(), childs.end(), entrychild) - childs.begin();
            int jstep, endptrick;
            if (j & 1) {
                j -= L;
                jstep = 1;
                endptrick = 0;
            } else {
                jstep = -1;
                endptrick = 1;
            }
            int p = labelend[b];
            while (j != 0) {
                label[endpoint[p ^ 1]] = 0;
                label[endpoint[at(endps, j - endptrick) ^ endptrick ^ 1]] = 0;
                assignLabel(endpoint[p ^ 1], 2, p);
                allowedge[at(endps, j - endptrick) >> 1] = 1;
                j += jstep;
                p = at(endps, j - endptrick) ^ endptrick;
                allowedge[p >> 1] = 1;
                j += jstep;
            }
            int bv = at(childs, j);
            label[endpoint[p ^ 1]] = label[bv] = 2;
            labelend[endpoint[p ^ 1]] = labelend[bv] = p;
            bestedge[bv] = -1;
            j += jstep;
            while (at(childs, j) != entrychild) {
                bv = at(childs, j);
                if (label[bv] == 1) {
                    j += jstep;
                    continue;
                }
                vector<int> lv;
                leaves(bv, lv);
                int found = -1;
                for (int x : lv)
                    if (label[x] != 0) {
                        found = x;
                        break;
                    }
                if (found >= 0) {
                    label[found] = 0;
                    label[endpoint[mate[blossombase[bv]]]] = 0;
                    assignLabel(found, 2, labelend[found]);
                }
                j += jstep;
            }
        }
        label[b] = labelend[b] = -1;
        blossomchilds[b].clear();
        blossomendps[b].clear();
        blossombase[b] = -1;
        blossombestedges[b].clear();
        hasBestList[b] = 0;
        bestedge[b] = -1;
        unusedblossoms.push_back(b);
    }

    void augmentBlossom(int b, int v) {
        int t = v;
        while (blossomparent[t] != b) t = blossomparent[t];
        if (t >= nv) augmentBlossom(t, v);
        vector<int>& childs = blossomchilds[b];
        vector<int>& endps = blossomendps[b];
        int L = childs.size();
        auto at = [&](vector<int>& vec, int idx) -> int& { return vec[((idx % L) + L) % L]; };
        int i = find(childs.begin(), childs.end(), t) - childs.begin();
        int j = i, jstep, endptrick;
        if (i & 1) {
            j -= L;
            jstep = 1;
            endptrick = 0;
        } else {
            jstep = -1;
            endptrick = 1;
        }
        while (j != 0) {
            j += jstep;
            t = at(childs, j);
            int p = at(endps, j - endptrick) ^ endptrick;
            if (t >= nv) augmentBlossom(t, endpoint[p]);
            j += jstep;
            t = at(childs, j);
            if (t >= nv) augmentBlossom(t, endpoint[p ^ 1]);
            mate[endpoint[p]] = p ^ 1;
            mate[endpoint[p ^ 1]] = p;
        }
        rotate(childs.begin(), childs.begin() + i, childs.end());
        rotate(endps.begin(), endps.begin() + i, endps.end());
        blossombase[b] = blossombase[childs[0]];
    }

    void augmentMatching(int k) {
        int ends[2][2] = {{(int)edges[k][0], 2 * k + 1}, {(int)edges[k][1], 2 * k}};
        for (auto& sp : ends) {
            int s = sp[0], p = sp[1];
            while (true) {
                int bs = inblossom[s];
                if (bs >= nv) augmentBlossom(bs, s);
                mate[s] = p;
                if (labelend[bs] == -1) break;
                int t = endpoint[labelend[bs]];
                int bt = inblossom[t];
                s = endpoint[labelend[bt]];
                int j = endpoint[labelend[bt] ^ 1];
                if (bt >= nv) augmentBlossom(bt, j);
                mate[j] = labelend[bt];
                p = labelend[bt] ^ 1;
            }
        }
    }

    vector<int> solve(int n, const vector<array<ll, 3>>& input) {
        nv = n;
        edges = input;
        ne = edges.size();
        mate.assign(nv, -1);
        if (ne == 0) return mate;
        ll maxweight = 0;
        for (auto& e : edges) maxweight = max(maxweight, e[2]);
        endpoint.resize(2 * ne);
        for (int p = 0; p < 2 * ne; p++) endpoint[p] = edges[p >> 1][p & 1];
        neighbend.assign(nv, {});
        for (int k = 0; k < ne; k++) {
            neighbend[edges[k][0]].push_back(2 * k + 1);
            neighbend[edges[k][1]].push_back(2 * k);
        }
        label.assign(2 * nv, 0);
        labelend.assign(2 * nv, -1);
        inblossom.resize(nv);
        iota(inblossom.begin(), inblossom.end(), 0);
        blossomparent.assign(2 * nv, -1);
        blossomchilds.assign(2 * nv, {});
        blossombase.assign(2 * nv, -1);
        for (int v = 0; v < nv; v++) blossombase[v] = v;
        blossomendps.assign(2 * nv, {});
        bestedge.assign(2 * nv, -1);
        blossombestedges.assign(2 * nv, {});
        hasBestList.assign(2 * nv, 0);
        unusedblossoms.clear();
        for (int b = nv; b < 2 * nv; b++) unusedblossoms.push_back(b);
        dualvar.assign(2 * nv, 0);
        for (int v = 0; v < nv; v++) dualvar[v] = maxweight;
        allowedge.assign(ne, 0);

        for (int stage = 0; stage < nv; stage++) {
            fill(label.begin(), label.end(), 0);
            fill(bestedge.begin(), bestedge.end(), -1);
            for (int b = nv; b < 2 * nv; b++) {
                blossombestedges[b].clear();
                hasBestList[b] = 0;
            }
            fill(allowedge.begin(), allowedge.end(), 0);
            queue.clear();
            for (int v = 0; v < nv; v++)
                if (mate[v] == -1 && label[inblossom[v]] == 0) assignLabel(v, 1, -1);
            bool augmented = false;
            while (true) {
                while (!queue.empty() && !augmented) {
                    int v = queue.back();
                    queue.pop_back();
                    for (int p : neighbend[v]) {
                        int k = p >> 1, w = endpoint[p];
                        if (inblossom[v] == inblossom[w]) continue;
                        ll kslack = 0;
                        if (!allowedge[k]) {
                            kslack = slack(k);
                            if (kslack <= 0) allowedge[k] = 1;
                        }
                        if (allowedge[k]) {
                            if (label[inblossom[w]] == 0) {
                                assignLabel(w, 2, p ^ 1);
                            } else if (label[inblossom[w]] == 1) {
                                int base = scanBlossom(v, w);
                                if (base >= 0) {
                                    addBlossom(base, k);
                                } else {
                                    augmentMatching(k);
                                    augmented = true;
                                    break;
                                }
                            } else if (label[w] == 0) {
                                label[w] = 2;
                                labelend[w] = p ^ 1;
                            }
                        } else if (label[inblossom[w]] == 1) {
                            int b = inblossom[v];
                            if (bestedge[b] == -1 || kslack < slack(bestedge[b])) bestedge[b] = k;
                        } else if (label[w] == 0) {
                            if (bestedge[w] == -1 || kslack < slack(bestedge[w])) bestedge[w] = k;
                        }
                    }
                }
                if (augmented) break;
                int deltatype = 1, deltaedge = -1, deltablossom = -1;
                ll delta = *min_element(dualvar.begin(), dualvar.begin() + nv);
                for (int v = 0; v < nv; v++)
                    if (label[inblossom[v]] == 0 && bestedge[v] != -1) {
                        ll d = slack(bestedge[v]);
                        if (d < delta) delta = d, deltatype = 2, deltaedge = bestedge[v];
                    }
                for (int b = 0; b < 2 * nv; b++)
                    if (blossomparent[b] == -1 && label[b] == 1 && bestedge[b] != -1) {
                        ll d = slack(bestedge[b]) / 2;
                        if (d < delta) delta = d, deltatype = 3, deltaedge = bestedge[b];
                    }
                for (int b = nv; b < 2 * nv; b++)
                    if (blossombase[b] >= 0 && blossomparent[b] == -1 && label[b] == 2 && dualvar[b] < delta)
                        delta = dualvar[b], deltatype = 4, deltablossom = b;
                for (int v = 0; v < nv; v++) {
                    int lb = label[inblossom[v]];
                    if (lb == 1) dualvar[v] -= delta;
                    else if (lb == 2) dualvar[v] += delta;
                }
                for (int b = nv; b < 2 * nv; b++)
                    if (blossombase[b] >= 0 && blossomparent[b] == -1) {
                        if (label[b] == 1) dualvar[b] += delta;
                        else if (label[b] == 2) dualvar[b] -= delta;
                    }
                if (deltatype == 1) break;
                if (deltatype == 2) {
                    allowedge[deltaedge] = 1;
                    int i = edges[deltaedge][0], j = edges[deltaedge][1];
                    if (label[inblossom[i]] == 0) swap(i, j);
                    queue.push_back(i);
                } else if (deltatype == 3) {
                    allowedge[deltaedge] = 1;
                    queue.push_back(edges[deltaedge][0]);
                } else {
                    expandBlossom(deltablossom, false);
                }
            }
            if (!augmented) break;
            for (int b = nv; b < 2 * nv; b++)
                if (blossomparent[b] == -1 && blossombase[b] >= 0 && label[b] == 1 && dualvar[b] == 0)
                    expandBlossom(b, true);
        }
        vector<int> result(nv, -1);
        for (int v = 0; v < nv; v++)
            if (mate[v] >= 0) result[v] = endpoint[mate[v]];
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    map<pair<int, int>, ll> best;
    for (int i = 0; i < m; i++) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        --u;
        --v;
        if (u == v) continue;
        if (u > v) swap(u, v);
        auto it = best.find({u, v});
        if (it == best.end()) best[{u, v}] = w;
        else it->second = max(it->second, w);
    }
    // Parallel offers collapse to the best one; doubled weights keep every
    // dual update integral.
    vector<array<ll, 3>> edges;
    for (auto& [key, w] : best) edges.push_back({key.first, key.second, 2 * w});
    Matcher matcher;
    vector<int> mate = matcher.solve(n, edges);
    ll total = 0;
    for (int v = 0; v < n; v++)
        if (mate[v] > v) total += best[{v, mate[v]}];
    cout << total << '\n';
}
