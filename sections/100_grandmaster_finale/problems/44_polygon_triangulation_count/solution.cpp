#include <bits/stdc++.h>
using namespace std;

// Every triangulation contains exactly one triangle on the edge (0, n-1); its
// apex k splits the polygon into the chains 0..k and k..n-1, each closed by
// an internal diagonal.  So T[i][j] (chain i..j closed by a valid chord) is
// the sum over k of T[i][k] T[k][j] with (i,k), (k,j) valid.  A chord is an
// internal diagonal iff it lies in the interior angle at both ends and
// properly crosses no polygon edge (no three vertices are collinear).

typedef long long ll;
const ll MOD = 1000000007;

int n;
vector<ll> X, Y;

ll cross(int a, int b, int c) { return (X[b] - X[a]) * (Y[c] - Y[a]) - (Y[b] - Y[a]) * (X[c] - X[a]); }
int sgn(__int128 v) { return v > 0 ? 1 : v < 0 ? -1 : 0; }
int crossSign(int a, int b, int c) {
    return sgn((__int128)(X[b] - X[a]) * (Y[c] - Y[a]) - (__int128)(Y[b] - Y[a]) * (X[c] - X[a]));
}

bool inCone(int a, int b) {
    int a0 = (a + n - 1) % n, a1 = (a + 1) % n;
    if (crossSign(a0, a, a1) >= 0) return crossSign(a, b, a0) > 0 && crossSign(b, a, a1) > 0;
    return !(crossSign(a, b, a1) >= 0 && crossSign(b, a, a0) >= 0);
}

bool crossesBoundary(int a, int b) {
    for (int c = 0; c < n; c++) {
        int d = (c + 1) % n;
        if (c == a || c == b || d == a || d == b) continue;
        if ((crossSign(a, b, c) > 0) == (crossSign(a, b, d) > 0)) continue;
        if ((crossSign(c, d, a) > 0) != (crossSign(c, d, b) > 0)) return true;
    }
    return false;
}

int main() {
    cin >> n;
    X.resize(n);
    Y.resize(n);
    for (int i = 0; i < n; i++) cin >> X[i] >> Y[i];
    __int128 area2 = 0;
    for (int i = 0; i < n; i++) area2 += (__int128)X[i] * Y[(i + 1) % n] - (__int128)X[(i + 1) % n] * Y[i];
    if (area2 < 0) {
        reverse(X.begin(), X.end());
        reverse(Y.begin(), Y.end());
    }
    vector<vector<char>> ok(n, vector<char>(n, 0));
    for (int i = 0; i < n; i++) {
        ok[i][(i + 1) % n] = ok[(i + 1) % n][i] = 1;
        for (int j = i + 2; j < n; j++) {
            if (i == 0 && j == n - 1) continue;
            if (inCone(i, j) && inCone(j, i) && !crossesBoundary(i, j)) ok[i][j] = ok[j][i] = 1;
        }
    }
    vector<vector<ll>> T(n, vector<ll>(n, 0));
    for (int i = 0; i + 1 < n; i++) T[i][i + 1] = 1;
    for (int len = 2; len < n; len++)
        for (int i = 0; i + len < n; i++) {
            int j = i + len;
            if (!ok[i][j]) continue;
            ll total = 0;
            for (int k = i + 1; k < j; k++)
                if (ok[i][k] && ok[k][j]) total = (total + T[i][k] * T[k][j]) % MOD;
            T[i][j] = total;
        }
    cout << T[0][n - 1] << '\n';
}
