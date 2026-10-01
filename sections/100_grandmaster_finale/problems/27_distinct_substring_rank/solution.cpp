#include <bits/stdc++.h>
using namespace std;

// In suffix-array order, suffix sa[i] contributes the distinct substrings of
// lengths lcp[i]+1 .. n-sa[i], already in lexicographic order.  Prefix sums of
// these counts locate the k-th substring by binary search.  Its occurrences
// are the suffixes sa[i..hi] where lcp stays >= its length; a sparse table on
// lcp finds hi and another on sa gives the leftmost start.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    int q;
    cin >> s >> q;
    int n = s.size();
    vector<int> sa(n), rk(n), tmp(n);
    iota(sa.begin(), sa.end(), 0);
    for (int i = 0; i < n; i++) rk[i] = s[i];
    for (int k = 1;; k <<= 1) {
        auto key = [&](int i) { return pair(rk[i], i + k < n ? rk[i + k] : -1); };
        sort(sa.begin(), sa.end(), [&](int a, int b) { return key(a) < key(b); });
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; i++) tmp[sa[i]] = tmp[sa[i - 1]] + (key(sa[i - 1]) < key(sa[i]));
        rk = tmp;
        if (rk[sa[n - 1]] == n - 1) break;
    }
    vector<int> lcp(n, 0);
    for (int i = 0, h = 0; i < n; i++) {
        if (rk[i] == 0) {
            h = 0;
            continue;
        }
        int j = sa[rk[i] - 1];
        while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
        lcp[rk[i]] = h;
        if (h) h--;
    }
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (n - sa[i] - lcp[i]);
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;
    vector<vector<int>> mnL(LOG, lcp), mnS(LOG, sa);
    for (int k = 1; k < LOG; k++)
        for (int i = 0; i + (1 << k) <= n; i++) {
            mnL[k][i] = min(mnL[k - 1][i], mnL[k - 1][i + (1 << (k - 1))]);
            mnS[k][i] = min(mnS[k - 1][i], mnS[k - 1][i + (1 << (k - 1))]);
        }
    auto rangeMin = [&](vector<vector<int>>& t, int l, int r) {  // inclusive
        int k = 31 - __builtin_clz(r - l + 1);
        return min(t[k][l], t[k][r - (1 << k) + 1]);
    };
    string out;
    while (q--) {
        long long k;
        cin >> k;
        if (k > prefix[n]) {
            out += "-1\n";
            continue;
        }
        int i = lower_bound(prefix.begin() + 1, prefix.end(), k) - prefix.begin() - 1;
        int len = lcp[i] + (int)(k - prefix[i]);
        // Largest hi >= i with min(lcp[i+1..hi]) >= len.
        int lo = i, hi = n - 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (rangeMin(mnL, i + 1, mid) >= len) lo = mid;
            else hi = mid - 1;
        }
        int start = rangeMin(mnS, i, lo) + 1;
        out += to_string(start) + ' ' + to_string(len) + '\n';
    }
    cout << out;
}
