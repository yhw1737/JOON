#include <bits/stdc++.h>
using namespace std;
char get_grade(int score){
	return "FFFFFFDCBAA"[score/10];
}
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		cout << get_grade(n) << '\n';
	}
}