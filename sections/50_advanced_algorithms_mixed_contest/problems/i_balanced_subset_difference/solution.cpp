#include <bits/stdc++.h>
using namespace std;using ll=long long;
vector<ll>sums(const vector<ll>&a){vector<ll>s{0};for(ll x:a){int n=s.size();for(int i=0;i<n;i++)s.push_back(s[i]+x);}return s;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<ll>a(n);for(ll&x:a)cin>>x;vector<ll>l(a.begin(),a.begin()+n/2),r(a.begin()+n/2,a.end());auto L=sums(l),R=sums(r);sort(R.begin(),R.end());ll total=accumulate(a.begin(),a.end(),0LL),best=LLONG_MAX;for(ll x:L){ll need=total-2*x;ll threshold=need>=0?(need+1)/2:need/2;auto it=lower_bound(R.begin(),R.end(),threshold);if(it!=R.end())best=min(best,llabs(total-2*(x+*it)));if(it!=R.begin()){--it;best=min(best,llabs(total-2*(x+*it)));}}cout<<best<<'\n';}
