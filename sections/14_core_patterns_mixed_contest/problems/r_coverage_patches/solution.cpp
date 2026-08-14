#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long target;
    cin >> n >> target;
    vector<long long> values(n);
    for (long long &value : values) cin >> value;
    sort(values.begin(), values.end());
    long long covered = 0;
    int index = 0, patches = 0;
    while (covered < target) {
        if (index < n && values[index] <= covered + 1) {
            covered += values[index++];
        } else {
            covered += covered + 1;
            ++patches;
        }
    }
    cout << patches << '\n';
}
