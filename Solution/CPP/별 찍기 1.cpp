#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
	int n;
	cin >> n;
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<i;j++){
			cout << '*';
		}
		cout << endl;
	}
}