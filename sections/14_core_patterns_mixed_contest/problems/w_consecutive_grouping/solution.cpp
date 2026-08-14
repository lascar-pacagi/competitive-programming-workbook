#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> values(n);
    unordered_map<long long, int> remaining, need;
    for (long long &value : values) {
        cin >> value;
        ++remaining[value];
    }
    sort(values.begin(), values.end());
    for (long long value : values) {
        if (remaining[value] == 0) continue;
        if (need[value] > 0) {
            --remaining[value];
            --need[value];
            ++need[value + 1];
        } else if (remaining[value + 1] > 0
                   && remaining[value + 2] > 0) {
            --remaining[value];
            --remaining[value + 1];
            --remaining[value + 2];
            ++need[value + 3];
        } else {
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
}
