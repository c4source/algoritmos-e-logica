//Criar um programa que some duas matrizes de inteiros de mesmas dimensões

// escreva um programa que verifique se uma matriz quadrada é uma matriz de identidade. 

#include <stdio.h>
#define L 3 
#define C 3 

int main(){
    
    int mat1 [L][C];
    int mat2 [L][C];   
    int soma [L][C];
    
    //Leitura da primeira matriz.
    printf("Digite os elementos da primeira matriz:\n");
    for ( int i = 0; i < L; i++){
        for ( int j = 0; j < C; j++){
            scanf("%d ", &mat1[i][j]);
        }
    }
        
        
    // Leitura da segunda matriz. 
    printf("Digite os elementos da segunda matriz:\n");
    for (int i = 0; i < L; i++){
        for(int j = 0; j < C; j++){
            scanf("%d", &mat2[i][j]);
        }
    }
    
    //Soma das duas matrizes
    for (int i = 0; i < L; i++){
        for (int j = 0; j < C; j++){
            soma[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
    
    // Impressão da matriz soma 
    printf("==Matriz soma==\n");
    for (int i = 0; i < L; i ++){
        for (int j = 0; j < C; j++){
            printf("%4d ", soma[i][j]); // 4d para indentar 4 espaços
        }
        printf("\n");
    } 
    
    return 0;
    
}
