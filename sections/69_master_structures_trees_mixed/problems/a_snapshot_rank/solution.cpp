#include <bits/stdc++.h>
using namespace std;
struct Node {
  int left = 0, right = 0, count = 0;
};
vector<Node> tree(1);
int add(int old, int lo, int hi, int pos) {
  int node = tree.size();
  tree.push_back(tree[old]);
  tree[node].count++;
  if (lo != hi) {
    int mid = (lo + hi) / 2;
    if (pos <= mid)
      tree[node].left = add(tree[old].left, lo, mid, pos);
    else
      tree[node].right = add(tree[old].right, mid + 1, hi, pos);
  }
  return node;
}
int kth(int before, int after, int lo, int hi, int k) {
  if (lo == hi) return lo;
  int amount = tree[tree[after].left].count - tree[tree[before].left].count,
      mid = (lo + hi) / 2;
  if (k <= amount) return kth(tree[before].left, tree[after].left, lo, mid, k);
  return kth(tree[before].right, tree[after].right, mid + 1, hi, k - amount);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int maximum, q;
  if (!(cin >> maximum >> q)) return 0;
  int log = 20;
  while ((1 << log) <= q) log++;
  vector<vector<int>> up(log, vector<int>(q + 1));
  vector<int> root(q + 1), depth(q + 1);
  int versions = 0;
  auto ancestor = [&](int v, int steps) {
    for (int j = 0; j < log; j++)
      if (steps >> j & 1) v = up[j][v];
    return v;
  };
  while (q--) {
    char type;
    cin >> type;
    if (type == 'A') {
      int v, x;
      cin >> v >> x;
      ++versions;
      depth[versions] = depth[v] + 1;
      up[0][versions] = v;
      for (int j = 1; j < log; j++) up[j][versions] = up[j - 1][up[j - 1][versions]];
      root[versions] = add(root[v], 1, maximum, x);
    } else {
      int v, l, r, k;
      cin >> v >> l >> r >> k;
      int right_version = ancestor(v, depth[v] - r),
          left_version = ancestor(v, depth[v] - (l - 1));
      cout << kth(root[left_version], root[right_version], 1, maximum, k) << '\n';
    }
  }
}
