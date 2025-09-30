#include <stdio.h>
#define L 3 
#define C 3 

int main(){
    int mat[L][C];
        for (int i = 0; i < L; i++){
            for (int j = 0; j < C; j++){
                scanf("%d", &mat[i][j]);
            }
        }
    return 0; 
}  
