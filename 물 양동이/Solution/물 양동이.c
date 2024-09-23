#include<stdio.h>

int map[101][101] = {0};
int W, H;

void spread(int x, int y, int h){
    if (x<0 || y<0 || x>=W || y>=H || map[y][x]==0 || map[y][x]>h){
        return;
    }
    int temp = map[y][x];
    map[y][x] = 0;
    spread(x-1,y,temp);
    spread(x,y-1,temp);
    spread(x+1,y,temp);
    spread(x,y+1,temp);
}

int main() {
    int i, j, X, Y;
    scanf("%d %d", &W, &H);
    for(i=0;i<H;i++){
        for(j=0;j<W;j++){
            scanf("%d", &map[i][j]);
        }
    }
    scanf("%d %d", &X, &Y);
    spread(X-1,Y-1,map[Y-1][X-1]);
    for(i=0;i<H;i++){
        for(j=0;j<W;j++){
            printf("%d", map[i][j]);
            if (j!=W-1) printf(" ");
        }
        printf("\n");
    }
}
