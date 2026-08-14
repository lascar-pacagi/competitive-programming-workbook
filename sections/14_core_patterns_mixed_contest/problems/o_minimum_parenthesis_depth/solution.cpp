#include <bits/stdc++.h>
using namespace std;

bool feasible(const string &s, int limit) {
    int low = 0, high = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == '(') ++low, ++high;
        else if (s[i] == ')') --low, --high;
        else --low, ++high;
        int parity = (i + 1) & 1;
        if (low < 0) low = parity;
        high = min(high, limit);
        if ((high & 1) != parity) --high;
        if (low > high) return false;
    }
    return low == 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    if (s.size() % 2 || !feasible(s, (int)s.size())) {
        cout << -1 << '\n';
        return 0;
    }
    int low = 1, high = s.size();
    while (low < high) {
        int middle = low + (high - low) / 2;
        if (feasible(s, middle)) high = middle;
        else low = middle + 1;
    }
    cout << low << '\n';
}
