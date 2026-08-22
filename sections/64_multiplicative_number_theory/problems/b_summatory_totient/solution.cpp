#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int LIMIT = 1'000'000;
constexpr int64 MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int64> phi(LIMIT + 1);
    iota(phi.begin(), phi.end(), 0);
    for (int p = 2; p <= LIMIT; ++p)
        if (phi[p] == p)
            for (int multiple = p; multiple <= LIMIT; multiple += p)
                phi[multiple] -= phi[multiple] / p;
    for (int i = 1; i <= LIMIT; ++i)
        phi[i] = (phi[i] + phi[i - 1]) % MOD;

    unordered_map<int64, int64> memo;
    function<int64(int64)> summatory = [&](int64 n) -> int64 {
        if (n <= LIMIT) return phi[n];
        if (auto it = memo.find(n); it != memo.end()) return it->second;
        int64 answer = n % MOD * ((n + 1) % MOD) % MOD;
        answer = answer * ((MOD + 1) / 2) % MOD;
        for (int64 left = 2, right; left <= n; left = right + 1) {
            int64 quotient = n / left;
            right = n / quotient;
            int64 width = (right - left + 1) % MOD;
            answer = (answer - width * summatory(quotient)) % MOD;
        }
        if (answer < 0) answer += MOD;
        return memo[n] = answer;
    };

    int q;
    cin >> q;
    while (q--) {
        int64 n;
        cin >> n;
        cout << summatory(n) << '\n';
    }
}
