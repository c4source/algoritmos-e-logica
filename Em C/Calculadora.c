#include <stdio.h>


int main() {
    
    char operacao;
    
    int n1, n2; 
    printf("Numero 1: ");
    scanf("%i", &n1);
    printf("Numero 2: ");
    scanf("%i", &n2);
    printf("Operação desejada (+ , - , / *]: ");
    scanf(" %c", &operacao);
    
    switch (operacao){
        case '+': printf("%d + %d = %d\n", n1, n2, n1 + n2); break;
        case '-': printf("%d - %d = %d\n", n1, n2, n1 - n2); break;
        case '/': printf("%d / %d = %d\n", n1, n2, n1 / n2); break;
        case '*': printf("%d * %d = %d\n", n1, n2, n1 * n2); break; 
        default: printf("Operação inválida");
    }  
return 0; 
}
