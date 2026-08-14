#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tests;
    cin >> tests;
    while (tests--) {
        int n, position;
        string commands;
        cin >> n >> position >> commands;
        --position;
        vector<char> seen(n, false);
        seen[position] = true;
        int distinct = 1;
        for (char command : commands) {
            position = (position + (command == 'R' ? 1 : n - 1)) % n;
            if (!seen[position]) {
                seen[position] = true;
                ++distinct;
            }
        }
        cout << position + 1 << ' ' << distinct << '\n';
    }
}
