#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    constexpr int LEVELS = 61;
    vector<array<int, LEVELS>> up(n);
    vector<array<ll, LEVELS>> minimum(n);

    for (int vertex = 0; vertex < n; ++vertex) {
        cin >> up[vertex][0];
        --up[vertex][0];
    }

    vector<ll> value(n);
    for (ll& current : value)
        cin >> current;

    for (int vertex = 0; vertex < n; ++vertex)
        minimum[vertex][0] = value[up[vertex][0]];

    for (int level = 1; level < LEVELS; ++level) {
        for (int vertex = 0; vertex < n; ++vertex) {
            int middle = up[vertex][level - 1];
            up[vertex][level] = up[middle][level - 1];
            minimum[vertex][level] = min(
                minimum[vertex][level - 1],
                minimum[middle][level - 1]
            );
        }
    }

    while (q--) {
        int vertex;
        unsigned long long steps;
        cin >> vertex >> steps;
        --vertex;

        ll answer = value[vertex];
        for (int level = 0; level < LEVELS; ++level) {
            if ((steps >> level) & 1ULL) {
                answer = min(answer, minimum[vertex][level]);
                vertex = up[vertex][level];
            }
        }

        cout << vertex + 1 << ' ' << answer << '\n';
    }
}
