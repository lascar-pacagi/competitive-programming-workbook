#include <bits/stdc++.h>
using namespace std;
using ll=long long;
ll ways[20][172];
ll count_to(ll n,int target) {
    if(n<0)return 0;
    string digits=to_string(n);
    ll answer=0;
    int prefix=0;
    for(int pos=0;pos<(int)digits.size();pos++) {
        int limit=digits[pos]-'0',remaining=digits.size()-pos-1;
        for(int digit=0;digit<limit;digit++) {
            int needed=target-prefix-digit;
            if(0<=needed&&needed<=171)answer+=ways[remaining][needed];
        }
        prefix+=limit;
    }
    return answer+(prefix==target);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ways[0][0]=1;
    for(int length=1;length<20;length++)for(int total=0;total<=171;total++)for(int digit=0;digit<=9&&digit<=total;digit++)ways[length][total]+=ways[length-1][total-digit];
    int q;
    cin>>q;
    while(q--) {
        ll l,r;
        int target;
        cin>>l>>r>>target;
        cout<<count_to(r,target)-count_to(l-1,target)<<'\n';
    }
}
