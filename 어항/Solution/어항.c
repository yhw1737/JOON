#include<stdio.h>

int main() {
    int t, ans = 0;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        int k;
        scanf("%d",&k);
        ans+=k*(i+1);
    }
    printf("%d",ans);
}
