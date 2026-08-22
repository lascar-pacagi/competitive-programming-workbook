#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<int> queries(q);
    int maximum = 1;
    for (int& n : queries) {
        cin >> n;
        maximum = max(maximum, n);
    }

    vector<int> phi(maximum + 1);
    iota(phi.begin(), phi.end(), 0);
    for (int p = 2; p <= maximum; ++p) {
        if (phi[p] != p)
            continue;
        for (int multiple = p; multiple <= maximum; multiple += p)
            phi[multiple] -= phi[multiple] / p;
    }

    for (int n : queries) {
        long long answer = 0;
        for (int d = 1; 1LL * d * d <= n; ++d) {
            if (n % d != 0)
                continue;
            answer = (answer + 1LL * d * phi[n / d]) % MOD;
            int other = n / d;
            if (other != d)
                answer = (answer + 1LL * other * phi[d]) % MOD;
        }
        cout << answer << '\n';
    }
}
