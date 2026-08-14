#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;priority_queue<long long,vector<long long>,greater<long long>> q;while(n--){long long x;cin>>x;q.push(x);}long long ans=0;while(q.size()>1){long long a=q.top();q.pop();long long b=q.top();q.pop();ans+=a+b;q.push(a+b);}cout<<ans<<'\n';}
