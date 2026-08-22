#include <bits/stdc++.h>
using namespace std;
struct Node {
  int left = 0, right = 0, count = 0;
};
vector<Node> tree(1);
int update(int old, int lo, int hi, int position, int delta) {
  int node = tree.size();
  tree.push_back(tree[old]);
  tree[node].count += delta;
  if (lo != hi) {
    int mid = (lo + hi) / 2;
    if (position <= mid)
      tree[node].left = update(tree[old].left, lo, mid, position, delta);
    else
      tree[node].right = update(tree[old].right, mid + 1, hi, position, delta);
  }
  return node;
}
int prefix(int node, int lo, int hi, int x) {
  if (!node || x < lo) return 0;
  if (hi <= x) return tree[node].count;
  int mid = (lo + hi) / 2;
  return prefix(tree[node].left, lo, mid, x) + prefix(tree[node].right, mid + 1, hi, x);
}
int kth(int node, int lo, int hi, int k) {
  if (lo == hi) return lo;
  int mid = (lo + hi) / 2, left_count = tree[tree[node].left].count;
  if (k <= left_count) return kth(tree[node].left, lo, mid, k);
  return kth(tree[node].right, mid + 1, hi, k - left_count);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int maximum, q;
  if (!(cin >> maximum >> q)) return 0;
  vector<int> roots(1, 0);
  while (q--) {
    char type;
    int version, x;
    cin >> type >> version >> x;
    if (type == 'I' || type == 'E')
      roots.push_back(update(roots[version], 1, maximum, x, type == 'I' ? 1 : -1));
    else if (type == 'K')
      cout << kth(roots[version], 1, maximum, x) << '\n';
    else
      cout << prefix(roots[version], 1, maximum, x) << '\n';
  }
}
