#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; int n=s.size(); vector<int>p(n); for(int i=1;i<n;i++){int j=p[i-1];while(j&&s[i]!=s[j])j=p[j-1];if(s[i]==s[j])j++;p[i]=j;} int k=n-p.back(); cout<<(n%k==0?k:n)<<'\n';}
