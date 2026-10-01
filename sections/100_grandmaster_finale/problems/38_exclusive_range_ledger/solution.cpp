#include <bits/stdc++.h>
using namespace std;

// The XORs of subsets of a[l..r] form a vector space V over GF(2); every
// element of V is hit by exactly 2^{len - dim V} subsets.  Sweep r and keep a
// prefix basis in which each leading bit holds the most recent vector
// possible: an incoming element is swapped in whenever it is newer than the
// stored one.  Then the stored vectors with position >= l form an echelon
// basis of V, giving both dim V and membership of x.

const long long MOD = 1000000007;
const int BITS = 30;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (auto& v : a) cin >> v;
    vector<array<int, 4>> queries(q);
    for (int i = 0; i < q; i++) {
        int l, r, x;
        cin >> l >> r >> x;
        queries[i] = {r, l, x, i};
    }
    sort(queries.begin(), queries.end());
    vector<long long> pow2(n + 1, 1);
    for (int i = 0; i < n; i++) pow2[i + 1] = pow2[i] * 2 % MOD;
    array<int, BITS> basis{}, where{};
    vector<long long> answer(q);
    int done = 0;
    for (auto [r, l, x, idx] : queries) {
        while (done < r) {
            int v = a[done], p = ++done;
            for (int b = BITS - 1; b >= 0; b--) {
                if (!(v >> b & 1)) continue;
                if (!basis[b]) {
                    basis[b] = v;
                    where[b] = p;
                    break;
                }
                if (where[b] < p) swap(basis[b], v), swap(where[b], p);
                v ^= basis[b];
            }
        }
        int rank = 0;
        for (int b = BITS - 1; b >= 0; b--)
            if (basis[b] && where[b] >= l) {
                rank++;
                if (x >> b & 1) x ^= basis[b];
            }
        answer[idx] = x ? 0 : pow2[r - l + 1 - rank];
    }
    string out;
    for (long long v : answer) out += to_string(v) + '\n';
    cout << out;
}
