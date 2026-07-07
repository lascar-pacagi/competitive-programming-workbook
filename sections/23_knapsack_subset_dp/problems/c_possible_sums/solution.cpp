#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    int total = 0;
    for (int &x : a) {
        cin >> x;
        total += x;
    }
    vector<char> possible(total + 1, false);
    possible[0] = true;
    int current = 0;
    for (int x : a) {
        for (int s = current; s >= 0; s--) {
            if (possible[s]) possible[s + x] = true;
        }
        current += x;
    }
    vector<int> ans;
    for (int s = 1; s <= total; s++) {
        if (possible[s]) ans.push_back(s);
    }
    cout << ans.size() << '\n';
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << '\n';
    return 0;
}

