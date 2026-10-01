#include <bits/stdc++.h>
using namespace std;

// Pressing is linear over GF(2) and presses commute.  Fix the presses of the
// first row as unknowns; then each lamp of row r can only be switched off by
// the press below it, which determines row r+1 as an affine function of the
// unknowns.  The last row of lamps yields m equations in m unknowns: the
// answer is 2^(m - rank) if they are consistent and 0 otherwise.  Rows are
// bitsets of the m unknowns plus a constant bit.

const long long MOD = 1000000007;
const int MAXM = 1001;
typedef bitset<MAXM + 1> Row;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (auto& s : g) cin >> s;
    if (m > n) {
        vector<string> t(m, string(n, '0'));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) t[j][i] = g[i][j];
        g = t;
        swap(n, m);
    }
    vector<Row> prev(m), cur(m), nxt(m);
    for (int c = 0; c < m; c++) cur[c][c] = 1;
    auto lampRow = [&](int r, vector<Row>& out) {
        for (int c = 0; c < m; c++) {
            Row v = prev[c] ^ cur[c];
            if (c) v ^= cur[c - 1];
            if (c + 1 < m) v ^= cur[c + 1];
            if (g[r][c] == '1') v.flip(m);
            out[c] = v;
        }
    };
    for (int r = 0; r + 1 < n; r++) {
        lampRow(r, nxt);
        swap(prev, cur);
        swap(cur, nxt);
    }
    vector<Row> eqs(m);
    lampRow(n - 1, eqs);
    int rank = 0;
    for (int bit = 0; bit < m; bit++) {
        int pivot = -1;
        for (int i = rank; i < m; i++)
            if (eqs[i][bit]) {
                pivot = i;
                break;
            }
        if (pivot < 0) continue;
        swap(eqs[rank], eqs[pivot]);
        for (int i = 0; i < m; i++)
            if (i != rank && eqs[i][bit]) eqs[i] ^= eqs[rank];
        rank++;
    }
    for (int i = rank; i < m; i++)
        if (eqs[i][m]) {
            cout << 0 << '\n';
            return 0;
        }
    long long ans = 1;
    for (int i = 0; i < m - rank; i++) ans = ans * 2 % MOD;
    cout << ans << '\n';
}
