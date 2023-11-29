#include <bits/stdc++.h>
using namespace std;
int decimal(string s){
    int ss=s.size(), res = 0;
    for(int i=0;i<ss;i++){
        if (s[i]=='1'){
            res+=pow(2,ss-i-1);
        }
    }
    return res;
}
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    string a,b;
    int n,m;
    cin >> a >> b;
    n=decimal(a);
    m=decimal(b);
    cout << n+m;
}