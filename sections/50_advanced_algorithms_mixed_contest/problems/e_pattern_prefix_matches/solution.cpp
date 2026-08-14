#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string p,t;cin>>p>>t;string s=p+"#"+t;vector<int>z(s.size());for(int i=1,l=0,r=0;i<(int)s.size();i++){if(i<=r)z[i]=min(r-i+1,z[i-l]);while(i+z[i]<(int)s.size()&&s[z[i]]==s[i+z[i]])z[i]++;if(i+z[i]-1>r)l=i,r=i+z[i]-1;}for(int i=0;i<(int)t.size();i++)cout<<min((int)p.size(),z[p.size()+1+i])<<(i+1==(int)t.size()?'\n':' ');}
