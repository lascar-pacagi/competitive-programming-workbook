#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> score(n);
    for (long long& value : score) cin >> value;

    vector<int> incompatible(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        incompatible[u] |= 1 << v;
        incompatible[v] |= 1 << u;
    }

    int total_masks = 1 << n;
    vector<long long> total(total_masks, 0);
    vector<char> compatible(total_masks, false);
    compatible[0] = true;
    long long answer = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        int bit = __builtin_ctz(mask);
        int previous = mask ^ (1 << bit);
        total[mask] = total[previous] + score[bit];
        compatible[mask] = compatible[previous] &&
                           ((incompatible[bit] & previous) == 0);
        if (compatible[mask]) answer = max(answer, total[mask]);
    }

    cout << answer << '\n';
    return 0;
}
