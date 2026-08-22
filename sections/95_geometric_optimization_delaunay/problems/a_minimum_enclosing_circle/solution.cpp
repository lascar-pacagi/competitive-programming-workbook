#include <bits/stdc++.h>
using namespace std;
const double EPS=1e-10,PI=acos(-1.0);
struct P {
    double x,y;
    P operator+(P b)const {
        return {
            x+b.x,y+b.y
        }
        ;
    }
    P operator-(P b)const {
        return {
            x-b.x,y-b.y
        }
        ;
    }
    P operator*(double k)const {
        return {
            x*k,y*k
        }
        ;
    }
}
;
double cross(P a,P b) {
    return a.x*b.y-a.y*b.x;
}
double dot(P a,P b) {
    return a.x*b.x+a.y*b.y;
}
double norm(P a) {
    return hypot(a.x,a.y);
}
struct L {
    P p,v;
    double angle;
}
;
P meet(L a,L b) {
    double t=cross(b.p-a.p,b.v)/cross(a.v,b.v);
    return a.p+a.v*t;
}
struct C {
    P p;
    double r;
}
;
double overlap(C a,C b) {
    double d=norm(a.p-b.p);
    if(d>=a.r+b.r)return 0;
    if(d<=abs(a.r-b.r))return PI*min(a.r,b.r)*min(a.r,b.r);
    double x=acos(clamp((d*d+a.r*a.r-b.r*b.r)/(2*d*a.r),-1.0,1.0)),y=acos(clamp((d*d+b.r*b.r-a.r*a.r)/(2*d*b.r),-1.0,1.0));
    return a.r*a.r*x+b.r*b.r*y-d*a.r*sin(x);
}
int tangents(C a,C b) {
    double d=norm(a.p-b.p);
    if(d<=EPS)return abs(a.r-b.r)<=EPS?-1:0;
    int ans=0;
    for(double z:{abs(a.r-b.r),a.r+b.r})ans+=d>z+EPS?2:(abs(d-z)<=EPS);
    return ans;
}
C circle2(P a,P b) {
    P c=(a+b)*.5;
    return {
        c,norm(a-b)/2
    }
    ;
}
C circle3(P a,P b,P c) {
    double d=2*cross(b-a,c-a);
    double aa=dot(a,a),bb=dot(b,b),cc=dot(c,c);
    P o= {
        (aa*(b.y-c.y)+bb*(c.y-a.y)+cc*(a.y-b.y))/d,(aa*(c.x-b.x)+bb*(a.x-c.x)+cc*(b.x-a.x))/d
    }
    ;
    return {
        o,norm(o-a)
    }
    ;
}
C mec(vector<P>p) {
    mt19937 rng(947311);
    shuffle(p.begin(),p.end(),rng);
    C c {
        {
            0,0
        }
        ,-1
    }
    ;
    auto outside=[](P x,C c) {
        return c.r<0||norm(x-c.p)>c.r+1e-9;
    }
    ;
    for(int i=0;i<(int)p.size();i++)if(outside(p[i],c)) {
        c= {
            p[i],0
        }
        ;
        for(int j=0;j<i;j++)if(outside(p[j],c)) {
            c=circle2(p[i],p[j]);
            for(int k=0;k<j;k++)if(outside(p[k],c))c=circle3(p[i],p[j],p[k]);
        }
    }
    return c;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout<<fixed<<setprecision(10);
    int n;
    cin>>n;
    vector<P>p(n);
    for(auto&x:p)cin>>x.x>>x.y;
    C c=mec(p);
    cout<<c.p.x<<' '<<c.p.y<<' '<<c.r<<'\n';
}
