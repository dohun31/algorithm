#include <stdio.h>
#include <math.h>
#define NUM 16

int dfs(int queen[], int n, int row){
    int count = 0;
    // n개의 행에 퀸들이 있다면 종료
    if(n == row) {
        return 1;
    }

    for(int col = 0; col < n; col++) {
        queen[row] = col;
        int is_possible = 1;
        for(int x = 0; x < row; x++) {
            if (queen[x] == queen[row]) {
                is_possible = 0;
                break;
            }
            if (abs(queen[x] - queen[row]) == (row - x)) {
                is_possible = 0;
                break;
            }
        }
        if (is_possible) count += dfs(queen, n, row + 1);
    }
    return count;
}

int main(void){
    int n; scanf("%d", &n);
    int queen[NUM];
    printf("%d", dfs(queen, n, 0));
}