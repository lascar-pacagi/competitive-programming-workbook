#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    priority_queue<long long> low;
    priority_queue<long long, vector<long long>, greater<long long>> high;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        if (low.empty() || x <= low.top()) low.push(x);
        else high.push(x);
        if (low.size() < high.size()) {
            low.push(high.top());
            high.pop();
        }
        if (low.size() > high.size() + 1) {
            high.push(low.top());
            low.pop();
        }
        if (i) cout << ' ';
        cout << low.top();
    }
    cout << '\n';
    return 0;
}
