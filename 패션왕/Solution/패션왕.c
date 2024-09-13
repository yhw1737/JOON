#include<stdio.h>
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        int n,m,k;
        scanf("%d %d %d",&n,&m,&k);
        printf("%d\n",n*m*k);
    }
}
