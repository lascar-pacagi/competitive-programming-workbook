#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1'000'000'007;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int q; if (!(cin >> q)) return 0;
    vector<int> queries(q); int maximum = 1;
    for (int &n : queries) { cin >> n; maximum = max(maximum, n); }
    vector<int> smallest(maximum + 1), power(maximum + 1, 1);
    iota(smallest.begin(), smallest.end(), 0);
    for (int p = 2; 1LL * p * p <= maximum; ++p)
        if (smallest[p] == p)
            for (int multiple = p * p; multiple <= maximum; multiple += p)
                if (smallest[multiple] == multiple) smallest[multiple] = p;
    vector<long long> answer(maximum + 1); answer[1] = 1;
    for (int value = 2; value <= maximum; ++value) {
        int p = smallest[value], rest = value / p;
        if (rest % p) {
            power[value] = p;
            answer[value] = (2LL * p - 1) * answer[rest];
        } else {
            int previous_power = power[rest];
            power[value] = previous_power * p;
            answer[value] = p * answer[rest]
                + 1LL * (p - 1) * previous_power * answer[rest / previous_power];
        }
    }
    for (int n : queries) cout << answer[n] % MOD << '\n';
}
