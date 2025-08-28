#include <stdio.h>
#define LIMITE 10 

int main() {
    char resp = "n";
    do {
        int numero;
        printf("Insira um número para a tabuada: ");
        scanf("%d", &numero);
        
        int c = 0;
        do {
            printf("%d * %d = %d\n", numero, ++c, (numero * c));
        } while (c < LIMITE);
        
        printf("Deseja ver outra tabuada? [S/n] ");
        scanf("%c ", &resp);
    } while (resp == 's');
}
