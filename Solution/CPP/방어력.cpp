#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while(t--){
        double a, s, d, m;
        cin >> a >> s >> d >> m;
        cout << fixed;
        cout.precision(1);
        cout << a * floor(m * s) * (100 / (100 + d)) << '\n';
    }
}