#include <bits/stdc++.h>
using namespace std;

struct Row {
    string name;
    int score;
    int penalty;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<Row> rows(n);
        for (auto &row : rows) {
            cin >> row.name >> row.score >> row.penalty;
        }
        sort(rows.begin(), rows.end(), [](const Row &a, const Row &b) {
            if (a.score != b.score) return a.score > b.score;
            if (a.penalty != b.penalty) return a.penalty < b.penalty;
            return a.name < b.name;
        });
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << rows[i].name;
        }
        cout << '\n';
    }

    return 0;
}

