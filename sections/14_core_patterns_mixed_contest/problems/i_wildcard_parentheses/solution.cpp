#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tests;
    cin >> tests;
    while (tests--) {
        string s;
        cin >> s;
        int low = 0, high = 0;
        bool possible = s.size() % 2 == 0;
        for (int index = 0; index < (int)s.size(); ++index) {
            char c = s[index];
            if (c == '(') ++low, ++high;
            else if (c == ')') --low, --high;
            else --low, ++high;
            if (low < 0) low = (index + 1) & 1;
            if (high < 0) possible = false;
        }
        cout << (possible && low == 0 ? "YES" : "NO") << '\n';
    }
}
