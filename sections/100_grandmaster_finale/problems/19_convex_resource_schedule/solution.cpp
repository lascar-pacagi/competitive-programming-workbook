#include <bits/stdc++.h>
using namespace std; using i128=__int128_t; const i128 INF=(i128(1)<<120);
struct L{long long m; i128 b; int c;};
pair<i128,int> run(const vector<long long>&x,long long lam,bool mx){int n=x.size()-1;vector<optional<L>>t(4*(n+1));
 auto better=[&](const L&a,const L&b,long long z){i128 u=i128(a.m)*z+a.b,v=i128(b.m)*z+b.b;return u<v||(u==v&&(mx?a.c>b.c:a.c<b.c));};
 function<void(L,int,int,int)>add=[&](L z,int p,int l,int r){if(!t[p]){t[p]=z;return;}int md=(l+r)/2;bool le=better(z,*t[p],x[l]),mi=better(z,*t[p],x[md]);if(mi)swap(z,*t[p]);if(l==r)return;if(le!=mi)add(z,p*2,l,md);else if(better(z,*t[p],x[r])!=better(z,*t[p],x[md]))add(z,p*2+1,md+1,r);};
 function<L(int,int,int,int)>qry=[&](int at,int p,int l,int r){L z=*t[p];if(l==r)return z;int md=(l+r)/2,q=at<=md?p*2:p*2+1;if(!t[q])return z;L o=at<=md?qry(at,q,l,md):qry(at,q,md+1,r);return better(o,z,x[at])?o:z;};
 add({0,0,0},1,0,n);i128 val=0;int cnt=0;for(int i=1;i<=n;i++){L z=qry(i,1,0,n);val=i128(z.m)*x[i]+z.b+i128(x[i])*x[i]+lam;cnt=z.c+1;add({-2*x[i],val+i128(x[i])*x[i],cnt},1,0,n);}return {val,cnt};}
void print128(i128 x){if(x==0){cout<<0;return;}string s;while(x){s+=char('0'+x%10);x/=10;}reverse(s.begin(),s.end());cout<<s;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,k;if(!(cin>>n>>k))return 0;vector<long long>a(n),s(n+1);for(int i=0;i<n;i++){cin>>a[i];s[i+1]=s[i]+a[i];}if(k==1){print128(i128(s[n])*s[n]);cout<<'\n';return 0;}if(k==n){i128 z=0;for(auto v:a)z+=i128(v)*v;print128(z);cout<<'\n';return 0;}long long B=s[n]*s[n]+1,lo=-B,hi=B;while(lo<hi){long long md=lo+(hi-lo+1)/2;if(run(s,md,true).second>=k)lo=md;else hi=md-1;}auto [v,ma]=run(s,lo,true);int mi=run(s,lo,false).second;assert(mi<=k&&k<=ma);print128(v-i128(lo)*k);cout<<'\n';}
