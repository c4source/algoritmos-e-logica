#include <stdio.h>
#include <string.h> 
int main(){
    char nome[51];
    char nome2[51];
    
    printf("Digite seu nome: ");
    scanf("%50s", &nome);
    printf("Nome: %s\n", nome);
    getchar();
    
    printf("Digite um nome: ");
    fgets(nome2, sizeof(nome2), stdin);
    nome2[strcspn(nome2, "\n")] = '\0';
    printf("Nome 2: %s\n", nome2);
    
    return 0;
}    
