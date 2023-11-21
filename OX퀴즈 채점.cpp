#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t, n;
    cin >> t >> n;
    while(t--){
        int i, j, ans = 0;
        char m[100][100];
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                cin >> m[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if (m[i][j] == 'O'){
                    ans++;
                    if (i > 0){
                        if (m[i-1][j] == 'O'){
                            ans++;
                        }
                    }
                    if (i < n-1){
                        if (m[i+1][j] == 'O'){
                            ans++;
                        }
                    }if (j > 0){
                        if (m[i][j-1] == 'O'){
                            ans++;
                        }
                    }
                    if (j < n-1){
                        if (m[i][j+1] == 'O'){
                            ans++;
                        }
                    }
                }
            }
        }
        cout << ans << '\n';
    }
}