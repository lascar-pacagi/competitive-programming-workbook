#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> values(n);
        for (int &value : values) {
            cin >> value;
        }
        sort(values.begin(), values.end());
        int best = values[1] - values[0];
        for (int i = 2; i < n; ++i) {
            best = min(best, values[i] - values[i - 1]);
        }
        cout << best << '\n';
    }

    return 0;
}

