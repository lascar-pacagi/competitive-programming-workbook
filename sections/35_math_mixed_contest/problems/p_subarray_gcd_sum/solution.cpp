#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<pair<int, long long>> previous;
    long long answer = 0;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        vector<pair<int, long long>> current{{x, 1}};
        for (auto [g, count] : previous) {
            int next_gcd = gcd(g, x);
            if (current.back().first == next_gcd)
                current.back().second += count;
            else
                current.push_back({next_gcd, count});
        }
        for (auto [g, count] : current)
            answer = (answer + 1LL * g * count) % MOD;
        previous = move(current);
    }

    cout << answer << '\n';
}
