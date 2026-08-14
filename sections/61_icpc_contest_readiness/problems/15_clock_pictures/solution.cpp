#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;int n=s.size();vector<int>pi(n),cnt(n+1);for(int i=1;i<n;i++){int j=pi[i-1];while(j&&s[i]!=s[j])j=pi[j-1];if(s[i]==s[j])j++;pi[i]=j;}for(int x:pi)cnt[x]++;for(int i=n-1;i>0;i--)cnt[pi[i-1]]+=cnt[i];for(int i=1;i<=n;i++)cout<<cnt[i]+1<<(i==n?'\n':' ');}
