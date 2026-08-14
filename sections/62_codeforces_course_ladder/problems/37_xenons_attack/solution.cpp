#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    int size = 1;
    while (size < n) size <<= 1;

    vector<long long> tree(2 * size, -1);
    for (int i = 0; i < n; i++) cin >> tree[size + i];
    for (int v = size - 1; v >= 1; v--) {
        tree[v] = max(tree[2 * v], tree[2 * v + 1]);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int index;
            long long capacity;
            cin >> index >> capacity;
            int v = size + index - 1;
            tree[v] = capacity;
            for (v >>= 1; v > 0; v >>= 1) {
                tree[v] = max(tree[2 * v], tree[2 * v + 1]);
            }
        } else {
            long long need;
            cin >> need;
            if (tree[1] < need) {
                cout << 0 << '\n';
                continue;
            }
            int v = 1;
            while (v < size) {
                if (tree[2 * v] >= need) v = 2 * v;
                else v = 2 * v + 1;
            }
            cout << v - size + 1 << '\n';
        }
    }
    return 0;
}
