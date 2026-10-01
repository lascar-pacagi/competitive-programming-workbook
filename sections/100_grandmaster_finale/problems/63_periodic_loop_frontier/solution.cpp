#include <bits/stdc++.h>
using namespace std;

// a_N = number of Hamiltonian cycles of the W x N grid.  A broken-profile
// (plug) DP with bracket-encoded plugs produces a_1, a_2, ... row by row: the
// single cycle may only close at the last cell of a row with no other plug
// open.  Row-boundary profiles form a finite set U, so a_N = c^T T^(N-1) v
// satisfies a linear recurrence of order <= |U|.  Generate 2|U| + 8 terms,
// recover the recurrence by Berlekamp--Massey, and jump to N with
// Bostan--Mori.  (|U| = 1117 for W = 10, so powering T directly is too slow.)

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
    return C;
}

vector<ll> multiply(const vector<ll>& a, const vector<ll>& b) {
    if (a.empty() || b.empty()) return {};
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

ll nthTerm(const vector<ll>& seq, ll index) {
    if (index < (ll)seq.size()) return seq[index];
    vector<ll> Q = berlekampMassey(seq);
    int L = Q.size() - 1;
    if (L == 0) return 0;
    vector<ll> P = multiply(vector<ll>(seq.begin(), seq.begin() + L), Q);
    P.resize(L);
    while (index) {
        vector<ll> Qm = Q;
        for (size_t i = 1; i < Qm.size(); i += 2) Qm[i] = (MOD - Qm[i]) % MOD;
        vector<ll> U = multiply(P, Qm), V = multiply(Q, Qm), nP, nQ;
        for (size_t i = index & 1; i < U.size(); i += 2) nP.push_back(U[i]);
        for (size_t i = 0; i < V.size(); i += 2) nQ.push_back(V[i]);
        P = nP;
        Q = nQ;
        index >>= 1;
        if (P.empty()) return 0;
    }
    return P[0] * power(Q[0], MOD - 2) % MOD;
}

int W;

int partner(unsigned st, int k) {
    int depth = 0;
    if (((st >> (2 * k)) & 3) == 1) {
        for (int t = k;; t++) {
            unsigned v = (st >> (2 * t)) & 3;
            if (v == 1) depth++;
            else if (v == 2 && --depth == 0) return t;
        }
    }
    for (int t = k;; t--) {
        unsigned v = (st >> (2 * t)) & 3;
        if (v == 2) depth++;
        else if (v == 1 && --depth == 0) return t;
    }
}

int main() {
    ll N;
    cin >> W >> N;
    unsigned full = (1u << (2 * (W + 1))) - 1;
    unordered_map<unsigned, ll> cur, nxt;
    cur[0] = 1;
    unordered_set<unsigned> seen = {0};
    vector<ll> seq;
    while (true) {
        nxt.clear();
        for (auto& [st, c] : cur) {
            if (st >> (2 * W)) continue;
            unsigned ns = (st << 2) & full;
            nxt[ns] = (nxt[ns] + c) % MOD;
        }
        swap(cur, nxt);
        ll closed = 0;
        for (int j = 0; j < W; j++) {
            nxt.clear();
            int sj = 2 * j, sk = sj + 2;
            bool last = j + 1 == W;
            auto put = [&](unsigned key, ll c) {
                ll& slot = nxt[key];
                slot += c;
                if (slot >= MOD) slot -= MOD;
            };
            for (auto& [st, c] : cur) {
                unsigned L = (st >> sj) & 3, U = (st >> sk) & 3;
                unsigned base = st & ~(15u << sj);
                if (!L && !U) {
                    if (!last) put(base | (1u << sj) | (2u << sk), c);
                } else if (!L || !U) {
                    unsigned x = L | U;
                    put(base | (x << sj), c);
                    if (!last) put(base | (x << sk), c);
                } else if (L == 1 && U == 1) {
                    int p = partner(st, j + 1);
                    put((base & ~(3u << (2 * p))) | (1u << (2 * p)), c);
                } else if (L == 2 && U == 2) {
                    int p = partner(st, j);
                    put((base & ~(3u << (2 * p))) | (2u << (2 * p)), c);
                } else if (L == 2) {
                    put(base, c);
                } else if (last && base == 0) {
                    closed = (closed + c) % MOD;  // the single cycle closes here
                }
            }
            swap(cur, nxt);
        }
        for (auto& [st, c] : cur) seen.insert(st);
        seq.push_back(closed);
        if ((ll)seq.size() > N || seq.size() >= 2 * seen.size() + 8) break;
    }
    cout << nthTerm(seq, N - 1) << '\n';
}
