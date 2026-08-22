#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<int> queries(q);
    int maximum = 1;
    for (int& x : queries) {
        cin >> x;
        maximum = max(maximum, x);
    }

    vector<char> squarefree(maximum + 1, true);
    squarefree[0] = false;
    for (int p = 2; p * p <= maximum; ++p) {
        for (int multiple = p * p; multiple <= maximum; multiple += p * p)
            squarefree[multiple] = false;
    }

    vector<int> prefix(maximum + 1);
    for (int i = 1; i <= maximum; ++i)
        prefix[i] = prefix[i - 1] + squarefree[i];

    for (int x : queries)
        cout << prefix[x] << '\n';
}
