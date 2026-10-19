#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    int n;
    vector<int> count;

    void change(int node, int left, int right, int x, int delta) {
        if (right - left == 1) {
            count[node] = max(0, count[node] + delta);
            return;
        }
        int mid = (left + right) / 2;
        if (x < mid)
            change(2 * node, left, mid, x, delta);
        else
            change(2 * node + 1, mid, right, x, delta);
        count[node] = count[2 * node] + count[2 * node + 1];
    }

    int prefix(int node, int left, int right, int end) const {
        if (end <= left)
            return 0;
        if (right <= end)
            return count[node];
        int mid = (left + right) / 2;
        return prefix(2 * node, left, mid, end) +
               prefix(2 * node + 1, mid, right, end);
    }

    int kth(int node, int left, int right, int k) const {
        if (right - left == 1)
            return left + 1;
        int mid = (left + right) / 2;
        if (k <= count[2 * node])
            return kth(2 * node, left, mid, k);
        return kth(2 * node + 1, mid, right, k - count[2 * node]);
    }

  public:
    explicit SegmentTree(int size) : n(size), count(4 * size) {
    }

    void change(int score, int delta) {
        change(1, 0, n, score - 1, delta);
    }

    int prefix(int score) const {
        return prefix(1, 0, n, score);
    }

    int kth(int k) const {
        return k > count[1] ? -1 : kth(1, 0, n, k);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, q;
    if (!(cin >> m >> q))
        return 0;
    SegmentTree tree(m);
    while (q--) {
        int op, x;
        cin >> op >> x;
        if (op == 1)
            tree.change(x, 1);
        else if (op == 2)
            tree.change(x, -1);
        else if (op == 3)
            cout << tree.kth(x) << '\n';
        else
            cout << tree.prefix(x) << '\n';
    }
}
