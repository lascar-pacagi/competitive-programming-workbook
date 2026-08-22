#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int LIMIT = 1'000'000;
constexpr int64 MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int64> prefix(LIMIT + 1);
    iota(prefix.begin(), prefix.end(), 0);
    for (int prime = 2; prime <= LIMIT; ++prime)
        if (prefix[prime] == prime)
            for (int multiple = prime; multiple <= LIMIT; multiple += prime)
                prefix[multiple] -= prefix[multiple] / prime;
    for (int value = 1; value <= LIMIT; ++value)
        prefix[value] = (prefix[value] + prefix[value - 1]) % MOD;

    unordered_map<int64, int64> memo;
    function<int64(int64)> sum_phi = [&](int64 n) -> int64 {
        if (n <= 0) return 0;
        if (n <= LIMIT) return prefix[n];
        if (auto it = memo.find(n); it != memo.end()) return it->second;
        int64 answer = n % MOD * ((n + 1) % MOD) % MOD * ((MOD + 1) / 2) % MOD;
        for (int64 left = 2, right; left <= n; left = right + 1) {
            int64 quotient = n / left;
            right = n / quotient;
            answer = (answer - (right - left + 1) % MOD * sum_phi(quotient)) % MOD;
        }
        if (answer < 0) answer += MOD;
        return memo[n] = answer;
    };

    int q;
    cin >> q;
    while (q--) {
        int64 left, right;
        cin >> left >> right;
        cout << (sum_phi(right) - sum_phi(left - 1) + MOD) % MOD << '\n';
    }
}
