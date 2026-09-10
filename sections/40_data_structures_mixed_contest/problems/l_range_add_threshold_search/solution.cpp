#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct SegmentTree {
  int n;
  vector<ll> maximum, lazy;

  explicit SegmentTree(const vector<ll> &values)
      : n(values.size()), maximum(4 * n), lazy(4 * n) {
    build(1, 0, n, values);
  }

  void build(int node, int left, int right, const vector<ll> &values) {
    if (right - left == 1) {
      maximum[node] = values[left];
      return;
    }
    int middle = (left + right) / 2;
    build(2 * node, left, middle, values);
    build(2 * node + 1, middle, right, values);
    pull(node);
  }

  void pull(int node) {
    maximum[node] = max(maximum[2 * node], maximum[2 * node + 1]);
  }

  void apply(int node, ll delta) {
    maximum[node] += delta;
    lazy[node] += delta;
  }

  void push(int node) {
    if (lazy[node] == 0)
      return;
    apply(2 * node, lazy[node]);
    apply(2 * node + 1, lazy[node]);
    lazy[node] = 0;
  }

  void add(int node, int left, int right, int query_left, int query_right,
           ll delta) {
    if (right <= query_left || query_right <= left)
      return;
    if (query_left <= left && right <= query_right) {
      apply(node, delta);
      return;
    }
    push(node);
    int middle = (left + right) / 2;
    add(2 * node, left, middle, query_left, query_right, delta);
    add(2 * node + 1, middle, right, query_left, query_right, delta);
    pull(node);
  }

  int first_at_least(int node, int left, int right, int query_left,
                     int query_right, ll threshold) {
    if (right <= query_left || query_right <= left ||
        maximum[node] < threshold)
      return -1;
    if (right - left == 1)
      return left;
    push(node);
    int middle = (left + right) / 2;
    int answer = first_at_least(2 * node, left, middle, query_left,
                                query_right, threshold);
    if (answer != -1)
      return answer;
    return first_at_least(2 * node + 1, middle, right, query_left,
                          query_right, threshold);
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, q;
  if (!(cin >> n >> q))
    return 0;

  vector<ll> values(n);
  for (ll &value : values)
    cin >> value;

  SegmentTree tree(values);
  while (q--) {
    char operation;
    int left, right;
    ll x;
    cin >> operation >> left >> right >> x;
    --left;

    if (operation == 'A') {
      tree.add(1, 0, n, left, right, x);
    } else {
      int answer = tree.first_at_least(1, 0, n, left, right, x);
      cout << (answer == -1 ? -1 : answer + 1) << '\n';
    }
  }
}
