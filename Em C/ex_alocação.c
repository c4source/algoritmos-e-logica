#include <stdio.h>
#include <stdlib.h>

int main () {
    int t;
    printf("Informe o tamanho do vetor: ");
    scanf("%d", &t);
    if (t > 0) {
        int *ptr = (int*) malloc(t*sizeof(int));
        for(int i = 0; i < t; i++){
            printf("Informe o valor da posicao: %d: ", i);
            scanf("%d", &ptr[i]);
        }    
        int soma = 0;
        for(int i = 0; i < t; i++){
            soma += ptr[i];
        }
        printf("A soma dos valores informados é %d", soma);
        free(ptr);
        ptr = NULL;



    }else{
        printf("O valor informado deve ser maior que zero");

    }
    return 0; 


}