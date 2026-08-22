#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<pair<int, int>> queries(q);
    int maximum = 1;
    for (auto& [a, b] : queries) {
        cin >> a >> b;
        maximum = max(maximum, min(a, b));
    }

    vector<int> mu(maximum + 1), primes;
    vector<char> composite(maximum + 1);
    mu[1] = 1;
    for (int i = 2; i <= maximum; ++i) {
        if (!composite[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            if (1LL * i * p > maximum)
                break;
            composite[i * p] = true;
            if (i % p == 0)
                mu[i * p] = 0;
            else
                mu[i * p] = -mu[i];
            if (i % p == 0)
                break;
        }
    }

    vector<int> prefix(maximum + 1);
    for (int i = 1; i <= maximum; ++i)
        prefix[i] = prefix[i - 1] + mu[i];

    for (auto [a, b] : queries) {
        long long answer = 0;
        int left = 1;
        int limit = min(a, b);
        while (left <= limit) {
            int qa = a / left;
            int qb = b / left;
            int right = min(limit, min(a / qa, b / qb));
            long long coefficient = prefix[right] - prefix[left - 1];
            answer = (answer + coefficient * qa % MOD * qb) % MOD;
            left = right + 1;
        }
        cout << (answer + MOD) % MOD << '\n';
    }
}
