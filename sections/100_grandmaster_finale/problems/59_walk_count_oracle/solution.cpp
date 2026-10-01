#include <bits/stdc++.h>
using namespace std;

// a[i] = number of walks of length i from s to t = e_s^T A^i e_t.
// By Cayley--Hamilton the sequence satisfies a linear recurrence of order at
// most n, so 2n terms (each one sparse vector step) determine it through
// Berlekamp--Massey.  The N-th term is then [x^N] P(x)/Q(x), extracted by
// Bostan--Mori halving in O(n^2 log N).

typedef long long ll;
const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1;
    b %= MOD;
    while (e) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return r;
}

vector<ll> berlekampMassey(const vector<ll>& s) {
    vector<ll> C = {1}, B = {1};
    int L = 0, m = 1;
    ll b = 1;
    for (size_t i = 0; i < s.size(); i++) {
        ll d = 0;
        for (int j = 0; j <= L; j++) d = (d + C[j] * s[i - j]) % MOD;
        if (d == 0) {
            m++;
            continue;
        }
        vector<ll> T = C;
        ll coef = d * power(b, MOD - 2) % MOD;
        if (C.size() < B.size() + m) C.resize(B.size() + m, 0);
        for (size_t j = 0; j < B.size(); j++) C[j + m] = (C[j + m] - coef * B[j] % MOD + MOD) % MOD;
        if (2 * L <= (int)i) {
            L = i + 1 - L;
            B = T;
            b = d;
            m = 1;
        } else {
            m++;
        }
    }
    C.resize(L + 1);
    return C;  // Q(x) = C(x): sum_j C[j] a[i-j] = 0 for i >= L
}

vector<ll> multiply(const vector<ll>& a, const vector<ll>& b) {
    vector<unsigned long long> r(a.size() + b.size() - 1, 0);
    for (size_t i = 0; i < a.size(); i++) {
        if (!a[i]) continue;
        for (size_t j = 0; j < b.size(); j++) {
            r[i + j] += (unsigned long long)a[i] * b[j];
            if (r[i + j] >= (1ULL << 62)) r[i + j] %= MOD;
        }
    }
    vector<ll> out(r.size());
    for (size_t i = 0; i < r.size(); i++) out[i] = r[i] % MOD;
    return out;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s, t;
    ll N;
    cin >> n >> m >> N >> s >> t;
    --s;
    --t;
    vector<int> eu(m), ev(m);
    for (int i = 0; i < m; i++) {
        cin >> eu[i] >> ev[i];
        --eu[i];
        --ev[i];
    }
    int terms = 2 * n + 2;
    vector<ll> seq(terms), cur(n, 0), nxt(n);
    cur[s] = 1;
    for (int i = 0; i < terms; i++) {
        seq[i] = cur[t];
        fill(nxt.begin(), nxt.end(), 0);
        for (int e = 0; e < m; e++) {
            nxt[ev[e]] += cur[eu[e]];
            if (nxt[ev[e]] >= MOD) nxt[ev[e]] -= MOD;
        }
        swap(cur, nxt);
    }
    if (N < terms) {
        cout << seq[N] << '\n';
        return 0;
    }
    vector<ll> Q = berlekampMassey(seq);
    int L = Q.size() - 1;
    if (L == 0) {
        cout << 0 << '\n';
        return 0;
    }
    vector<ll> P = multiply(vector<ll>(seq.begin(), seq.begin() + L), Q);
    P.resize(L);
    while (N > 0) {
        vector<ll> Qm = Q;
        for (size_t i = 1; i < Qm.size(); i += 2) Qm[i] = (MOD - Qm[i]) % MOD;
        vector<ll> U = multiply(P, Qm), V = multiply(Q, Qm);
        vector<ll> nP, nQ;
        for (size_t i = N & 1; i < U.size(); i += 2) nP.push_back(U[i]);
        for (size_t i = 0; i < V.size(); i += 2) nQ.push_back(V[i]);
        P = nP;
        Q = nQ;
        N >>= 1;
        if (P.empty()) {
            cout << 0 << '\n';
            return 0;
        }
    }
    cout << P[0] * power(Q[0], MOD - 2) % MOD << '\n';
}
