#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1000000007, BASE = 911382323;
vector<ll> pw = {1};
mt19937 rng(712367821);
struct N {
  ll v, sum, hf, hr, add = 0;
  uint32_t p = rng();
  int z = 1;
  bool rev = 0;
  N *l = 0, *r = 0;
  N(ll v) : v(v), sum(v), hf((v % MOD + MOD) % MOD), hr(hf) {}
};
int sz(N *t) { return t ? t->z : 0; }
ll sm(N *t) { return t ? t->sum : 0; }
void ensure(int n) {
  while ((int)pw.size() <= n)
    pw.push_back(pw.back() * BASE % MOD);
}
void pull(N *t) {
  if (!t)
    return;
  ensure(sz(t->l) + sz(t->r) + 1);
  t->z = 1 + sz(t->l) + sz(t->r);
  t->sum = t->v + sm(t->l) + sm(t->r);
  int l = sz(t->l), r = sz(t->r);
  ll lf = t->l ? t->l->hf : 0, rf = t->r ? t->r->hf : 0,
     lr = t->l ? t->l->hr : 0, rr = t->r ? t->r->hr : 0;
  t->hf = (lf + t->v * pw[l] + rf * pw[l + 1]) % MOD;
  t->hr = (rr + t->v * pw[r] + lr * pw[r + 1]) % MOD;
}
void add(N *t, ll x) {
  if (t)
    t->v += x, t->sum += x * t->z, t->add += x;
}
void reverse_node(N *t) {
  if (t)
    swap(t->l, t->r), swap(t->hf, t->hr), t->rev ^= 1;
}
void push(N *t) {
  if (!t)
    return;
  if (t->rev)
    reverse_node(t->l), reverse_node(t->r), t->rev = 0;
  if (t->add)
    add(t->l, t->add), add(t->r, t->add), t->add = 0;
}
pair<N *, N *> split(N *t, int k) {
  if (!t)
    return {};
  push(t);
  if (sz(t->l) >= k) {
    auto [a, b] = split(t->l, k);
    t->l = b;
    pull(t);
    return {a, t};
  }
  auto [a, b] = split(t->r, k - sz(t->l) - 1);
  t->r = a;
  pull(t);
  return {t, b};
}
N *merge(N *a, N *b) {
  if (!a || !b)
    return a ? a : b;
  if (a->p > b->p) {
    push(a);
    a->r = merge(a->r, b);
    pull(a);
    return a;
  }
  push(b);
  b->l = merge(a, b->l);
  pull(b);
  return b;
}
void output(N *t) {
  if (!t)
    return;
  push(t);
  output(t->l);
  cout << t->v << ' ';
  output(t->r);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  N *root = 0;
  for (int i = 0; i < n; i++) {
    ll x;
    cin >> x;
    root = merge(root, new N(x));
  }
  while (q--) {
    string op;
    int l, r;
    cin >> op >> l >> r;
    auto [a, x] = split(root, l - 1);
    auto [b, c] = split(x, r - l + 1);
    if (op == "ADD") {
      ll v;
      cin >> v;
      add(b, v);
    } else if (op == "REV")
      reverse_node(b);
    else
      cout << sm(b) << '\n';
    root = merge(merge(a, b), c);
  }
}