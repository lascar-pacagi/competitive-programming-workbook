#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct Node {
  int left = 0, right = 0;
  int64 sum = 0, lazy = 0;
};
vector<Node> tree(1);
int build(const vector<int64>& a, int lo, int hi) {
  int node = tree.size();
  tree.push_back({});
  if (lo == hi)
    tree[node].sum = a[lo];
  else {
    int mid = (lo + hi) / 2;
    tree[node].left = build(a, lo, mid);
    tree[node].right = build(a, mid + 1, hi);
    tree[node].sum = tree[tree[node].left].sum + tree[tree[node].right].sum;
  }
  return node;
}
int update(int old, int lo, int hi, int ql, int qr, int64 value) {
  int node = tree.size();
  tree.push_back(tree[old]);
  if (ql <= lo && hi <= qr) {
    tree[node].sum += value * (hi - lo + 1);
    tree[node].lazy += value;
    return node;
  }
  int mid = (lo + hi) / 2;
  if (ql <= mid) tree[node].left = update(tree[old].left, lo, mid, ql, qr, value);
  if (qr > mid) tree[node].right = update(tree[old].right, mid + 1, hi, ql, qr, value);
  tree[node].sum = tree[tree[node].left].sum + tree[tree[node].right].sum +
                   tree[node].lazy * (hi - lo + 1);
  return node;
}
int64 query(int node, int lo, int hi, int ql, int qr, int64 carry = 0) {
  if (ql <= lo && hi <= qr) return tree[node].sum + carry * (hi - lo + 1);
  carry += tree[node].lazy;
  int mid = (lo + hi) / 2, res = 0;
  if (ql <= mid) res += query(tree[node].left, lo, mid, ql, qr, carry);
  if (qr > mid) res += query(tree[node].right, mid + 1, hi, ql, qr, carry);
  return res;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  vector<int64> a(n + 1);
  for (int i = 1; i <= n; i++) cin >> a[i];
  vector<int> roots{build(a, 1, n)};
  while (q--) {
    char type;
    int v, l, r;
    cin >> type >> v >> l >> r;
    if (type == 'A') {
      int64 x;
      cin >> x;
      roots.push_back(update(roots[v], 1, n, l, r, x));
    } else
      cout << query(roots[v], 1, n, l, r) << '\n';
  }
}
