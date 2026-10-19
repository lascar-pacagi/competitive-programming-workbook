#include <bits/stdc++.h>
using namespace std;

struct Node { int sum = 0, low = 0; };
Node merge_nodes(Node a, Node b) {
    return {a.sum+b.sum, min(a.low, a.sum+b.low)};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    string s; cin >> s;
    int size = 1;
    while (size < n) size *= 2;
    vector<Node> tree(2*size);
    for (int i = 0; i < n; i++) {
        int x = s[i] == '(' ? 1 : -1;
        tree[size+i] = {x, min(0, x)};
    }
    for (int v = size-1; v > 0; v--)
        tree[v] = merge_nodes(tree[2*v], tree[2*v+1]);
    while (q--) {
        char op; cin >> op;
        if (op == 'T') {
            int i; cin >> i;
            int v = size+i-1, x = -tree[v].sum;
            tree[v] = {x, min(0, x)};
            for (v /= 2; v > 0; v /= 2)
                tree[v] = merge_nodes(tree[2*v], tree[2*v+1]);
        } else {
            int l, r; cin >> l >> r;
            l += size-1; r += size;
            Node left, right;
            while (l < r) {
                if (l & 1) left = merge_nodes(left, tree[l++]);
                if (r & 1) right = merge_nodes(tree[--r], right);
                l /= 2; r /= 2;
            }
            Node answer = merge_nodes(left, right);
            cout << (answer.sum == 0 && answer.low >= 0 ? "YES" : "NO")
                 << '\n';
        }
    }
}
