#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    int log = 1;
    while ((1 << log) <= n) ++log;

    const long long INF = (1LL << 62);
    vector<long long> label(n + 1);
    for (int node = 1; node <= n; ++node) cin >> label[node];

    vector<vector<int>> up(log, vector<int>(n + 1, 0));
    vector<vector<long long>> minimum(log, vector<long long>(n + 1, INF));
    for (int node = 2; node <= n; ++node) cin >> up[0][node];
    for (int node = 1; node <= n; ++node) {
        minimum[0][node] = min(label[node], up[0][node] ? label[up[0][node]] : INF);
    }

    for (int bit = 1; bit < log; ++bit) {
        for (int node = 1; node <= n; ++node) {
            int middle = up[bit - 1][node];
            up[bit][node] = up[bit - 1][middle];
            minimum[bit][node] = min(minimum[bit - 1][node], minimum[bit - 1][middle]);
        }
    }

    while (q--) {
        int node;
        long long distance;
        cin >> node >> distance;
        long long answer = label[node];
        bool exists = true;
        for (int bit = 0; distance; ++bit, distance >>= 1LL) {
            if ((distance & 1LL) == 0) continue;
            if (bit >= log || up[bit][node] == 0) {
                exists = false;
                break;
            }
            answer = min(answer, minimum[bit][node]);
            node = up[bit][node];
        }
        cout << (exists ? answer : -1) << '\n';
    }
    return 0;
}
