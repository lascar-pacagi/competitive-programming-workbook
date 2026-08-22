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

    vector<long long> prefix(maximum + 1);
    for (int i = 1; i <= maximum; ++i)
        prefix[i] = (prefix[i - 1] + phi[i]) % MOD;

    for (int n : queries)
        cout << prefix[n] << '\n';
}
