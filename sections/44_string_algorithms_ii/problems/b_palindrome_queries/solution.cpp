#include <bits/stdc++.h>
using namespace std;

class RollingHash {
    static constexpr long long MOD1 = 1000000007;
    static constexpr long long MOD2 = 1000000009;
    static constexpr long long BASE = 911382323;
    vector<long long> h1, h2, p1, p2;

public:
    explicit RollingHash(const string& s) {
        int n = s.size();
        h1.assign(n + 1, 0);
        h2.assign(n + 1, 0);
        p1.assign(n + 1, 1);
        p2.assign(n + 1, 1);
        for (int i = 0; i < n; i++) {
            int value = s[i] - 'a' + 1;
            h1[i + 1] = (h1[i] * BASE + value) % MOD1;
            h2[i + 1] = (h2[i] * BASE + value) % MOD2;
            p1[i + 1] = p1[i] * BASE % MOD1;
            p2[i + 1] = p2[i] * BASE % MOD2;
        }
    }

    // Hash of s[l:r], with 0-based, half-open endpoints.
    pair<long long, long long> get(int l, int r) const {
        long long a = (h1[r] - h1[l] * p1[r - l]) % MOD1;
        long long b = (h2[r] - h2[l] * p2[r - l]) % MOD2;
        if (a < 0) {
            a += MOD1;
        }
        if (b < 0) {
            b += MOD2;
        }
        return {a, b};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) {
        return 0;
    }
    string reversed = s;
    reverse(reversed.begin(), reversed.end());
    RollingHash forward(s);
    RollingHash backward(reversed);
    int n = s.size();

    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--;  // Input [l, r] becomes the 0-based range [l - 1, r).
        bool same = forward.get(l, r) == backward.get(n - r, n - l);
        cout << (same ? "YES" : "NO") << '\n';
    }
}
