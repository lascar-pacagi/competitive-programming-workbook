#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<int>a(n);int total=0;for(int&x:a){cin>>x;total+=x;}vector<char>possible(total+1);possible[0]=1;for(int x:a)for(int s=total;s>=x;--s)if(possible[s-x])possible[s]=1;int ans=total;for(int s=0;s<=total/2;++s)if(possible[s])ans=min(ans,total-2*s);cout<<ans<<'\n';}
