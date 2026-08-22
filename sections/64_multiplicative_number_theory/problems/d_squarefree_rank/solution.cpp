#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<int64> queries(q);
    int64 largest = 0;
    for (int64 &k : queries) {
        cin >> k;
        largest = max(largest, k);
    }

    int limit = sqrtl(3.0L * largest) + 2;
    vector<int> mu(limit + 1), primes;
    vector<bool> composite(limit + 1);
    mu[1] = 1;
    for (int value = 2; value <= limit; ++value) {
        if (!composite[value]) {
            primes.push_back(value);
            mu[value] = -1;
        }
        for (int prime : primes) {
            if (1LL * value * prime > limit) break;
            composite[value * prime] = true;
            if (value % prime == 0) {
                mu[value * prime] = 0;
                break;
            }
            mu[value * prime] = -mu[value];
        }
    }

    auto count_squarefree = [&](int64 x) {
        int64 result = 0;
        for (int64 d = 1; d * d <= x; ++d)
            result += mu[d] * (x / (d * d));
        return result;
    };

    for (int64 k : queries) {
        int64 low = 1, high = 3 * k;
        while (low < high) {
            int64 middle = low + (high - low) / 2;
            if (count_squarefree(middle) >= k)
                high = middle;
            else
                low = middle + 1;
        }
        cout << low << '\n';
    }
}
