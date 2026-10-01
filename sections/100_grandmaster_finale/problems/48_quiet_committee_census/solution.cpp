#include <bits/stdc++.h>
using namespace std;

// Meet in the middle.  For the second half B, best[mask] / ways[mask] give the
// optimum and the number of optimal independent sets inside the vertex subset
// mask (branch on the lowest vertex: unused, or used with its neighbours
// removed).  Then enumerate the independent subsets S of the first half; each
// one leaves exactly B minus N(S) available.  O(2^(n/2)) time and memory.

typedef long long ll;
const ll MOD = 1000000007;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<ll> w(n);
    for (auto& x : w) scanf("%lld", &x);
    vector<unsigned long long> adj(n, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        --u;
        --v;
        adj[u] |= 1ULL << v;
        adj[v] |= 1ULL << u;
    }
    int h = n / 2, b = n - h;
    unsigned fullB = (1u << b) - 1;
    vector<unsigned> nbB(b);
    for (int i = 0; i < b; i++) nbB[i] = (unsigned)(adj[h + i] >> h) | (1u << i);
    vector<ll> best(1u << b, 0);
    vector<int> ways(1u << b, 1);
    for (unsigned mask = 1; mask < (1u << b); mask++) {
        int v = __builtin_ctz(mask);
        unsigned a = mask ^ (1u << v), c = mask & ~nbB[v];
        ll x = best[a], y = best[c] + w[h + v];
        if (x > y) best[mask] = x, ways[mask] = ways[a];
        else if (y > x) best[mask] = y, ways[mask] = ways[c];
        else best[mask] = x, ways[mask] = (ways[a] + ways[c]) % MOD;
    }
    unsigned size = 1u << h;
    vector<char> ok(size, 0);
    vector<ll> sum(size, 0);
    vector<unsigned> forb(size, 0);
    ok[0] = 1;
    ll top = -1, count = 0;
    for (unsigned mask = 0; mask < size; mask++) {
        if (mask) {
            int v = __builtin_ctz(mask);
            unsigned rest = mask ^ (1u << v);
            if (!ok[rest] || (adj[v] & rest)) continue;
            ok[mask] = 1;
            sum[mask] = sum[rest] + w[v];
            forb[mask] = forb[rest] | (unsigned)(adj[v] >> h);
        }
        unsigned freeB = fullB & ~forb[mask];
        ll value = sum[mask] + best[freeB];
        if (value > top) top = value, count = ways[freeB];
        else if (value == top) count = (count + ways[freeB]) % MOD;
    }
    printf("%lld %lld\n", top, count % MOD);
}
