#include <bits/stdc++.h>
using namespace std;

// A square ww whose root w = u^k (u primitive) lies inside a run of minimal
// period |u|, and inside one run the squares of half-length k|u| starting at
// x and x + |u| are equal.  So enumerate all runs, and for each run and each
// multiple L of its period, only the first min(p, #starts) starting positions;
// deduplicate those squares by hash.  Runs come from the runs theorem: under
// one of the two letter orders, every run contains a position i whose longest
// Lyndon word has length exactly the period.  Lyndon arrays and all
// longest-common-extension queries use polynomial hashing modulo 2^61 - 1.

typedef unsigned long long ull;
const ull MOD = (1ULL << 61) - 1, BASE = 1000003;

ull mulmod(ull a, ull b) {
    __uint128_t c = (__uint128_t)a * b;
    ull lo = (ull)(c & MOD), hi = (ull)(c >> 61);
    ull r = lo + hi;
    return r >= MOD ? r - MOD : r;
}

int n;
string s, rs;
vector<ull> pw, fh, rh;

ull getHash(const vector<ull>& h, int i, int len) {
    ull v = h[i + len] + MOD - mulmod(h[i], pw[len]);
    return v >= MOD ? v - MOD : v;
}

// Longest common prefix of suffixes starting at i and j of the string with
// prefix hashes h.
int extend(const string& t, const vector<ull>& h, int i, int j) {
    if (i == j) return n - i;
    int limit = n - max(i, j);
    if (limit == 0 || t[i] != t[j]) return 0;
    int good = 1, step = 1, hi;
    while (true) {
        long long nxt = (long long)good + step;
        if (nxt > limit || getHash(h, i, nxt) != getHash(h, j, nxt)) {
            hi = (int)min<long long>(nxt, limit + 1);
            break;
        }
        good = nxt;
        step *= 2;
    }
    int lo = good;
    while (hi - lo > 1) {
        int mid = (lo + hi) / 2;
        if (getHash(h, i, mid) == getHash(h, j, mid)) lo = mid;
        else hi = mid;
    }
    return lo;
}

int lce(int i, int j) { return extend(s, fh, i, j); }
int lcs(int i, int j) {  // common suffix of prefixes ending at i and j
    if (i < 0 || j < 0) return 0;
    return extend(rs, rh, n - 1 - i, n - 1 - j);
}

int main() {
    cin >> s;
    n = s.size();
    rs = string(s.rbegin(), s.rend());
    pw.assign(n + 1, 1);
    fh.assign(n + 1, 0);
    rh.assign(n + 1, 0);
    for (int i = 0; i < n; i++) {
        pw[i + 1] = mulmod(pw[i], BASE);
        fh[i + 1] = (mulmod(fh[i], BASE) + (ull)s[i]) % MOD;
        rh[i + 1] = (mulmod(rh[i], BASE) + (ull)rs[i]) % MOD;
    }
    vector<array<int, 3>> runs;
    vector<int> lyn(n);
    for (int flip = 0; flip < 2; flip++) {
        for (int i = n - 1; i >= 0; i--) {
            int j = i + 1;
            while (j < n) {
                int l = lce(i, j);
                if (j + l == n) break;  // suffix j is a prefix of suffix i
                bool smaller = s[i + l] < s[j + l];
                if (smaller != (bool)flip) j += lyn[j];
                else break;
            }
            lyn[i] = j - i;
        }
        for (int i = 0; i < n; i++) {
            int p = lyn[i], j = i + p;
            if (j > n) continue;
            int r = j < n ? lce(i, j) : 0;
            int l = lcs(i - 1, j - 1);
            if (l + r >= p) runs.push_back({i - l, j + r, p});
        }
    }
    sort(runs.begin(), runs.end());
    runs.erase(unique(runs.begin(), runs.end()), runs.end());
    vector<pair<ull, int>> squares;
    for (auto [a, b, p] : runs) {
        int length = b - a;
        for (int L = p; 2 * L <= length; L += p) {
            int lastStart = b - 2 * L;
            int upto = min(lastStart, a + p - 1);
            for (int x = a; x <= upto; x++) squares.push_back({getHash(fh, x, 2 * L), L});
        }
    }
    sort(squares.begin(), squares.end());
    squares.erase(unique(squares.begin(), squares.end()), squares.end());
    cout << squares.size() << '\n';
}
