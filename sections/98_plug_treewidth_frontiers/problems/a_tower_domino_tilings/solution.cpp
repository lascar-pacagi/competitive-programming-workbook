#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const int MOD=1e9+7;
using Mat=vector<vector<int>>;
Mat mul(const Mat&a,const Mat&b) {
    int n=a.size();
    Mat c(n,vector<int>(n));
    for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(a[i][k])for(int j=0;j<n;j++)c[i][j]=(c[i][j]+(ll)a[i][k]*b[k][j])%MOD;
    return c;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long h;
    int w;
    cin>>h>>w;
    int n=1<<w;
    Mat a(n,vector<int>(n));
    for(int in=0;in<n;in++) {
        function<void(int,int,int)>fill=[&](int c,int used,int out) {
            if(c==w) {
                a[in][out]++;
                return;
            }
            int bit=1<<c;
            if(used&bit)fill(c+1,used,out);
            else {
                if(c+1<w&&!(used&(bit<<1)))fill(c+2,used|bit|(bit<<1),out);
                fill(c+1,used|bit,out|bit);
            }
        }
        ;
        fill(0,in,0);
    }
    Mat r(n,vector<int>(n));
    for(int i=0;i<n;i++)r[i][i]=1;
    while(h) {
        if(h&1)r=mul(r,a);
        a=mul(a,a);
        h>>=1;
    }
    cout<<r[0][0]<<'\n';
}
