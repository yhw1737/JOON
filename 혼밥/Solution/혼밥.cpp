#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    vector<long long int> dp;
    dp.push_back(0);
    dp.push_back(1);
    for(int i=2;i<=n;i++){
        dp.push_back(dp[i-1]+dp[i-2]+1);
    }
    cout << dp[n];
}