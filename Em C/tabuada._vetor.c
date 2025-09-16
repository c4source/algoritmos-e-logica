#include <stdio.h>

int main(){
    int tabuada;
    printf("Digite a sua tabuada: \n");
    scanf("%d", &tabuada);
    getchar();
    
    int result[10];
    for (int i = 0; i < 10; i++) {
        result[i] = (i+1) * tabuada;
    }    
    for (int i = 0; i < 10; i++) {
        printf("%d x %d = %d\n", tabuada, (i+1), result[i]);
    }    
    return 0;    
    
}
