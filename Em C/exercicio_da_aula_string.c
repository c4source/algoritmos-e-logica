#include <stdio.h>
#include <string.h> 
int main(){
    
    char nome[51];
    char sobrenome[51];
    char email[51];
    int datanascimento, celular;
    
    printf("Digite seu nome: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0';
    printf("Nome: %s\n", nome); 
    
    
    printf("Digite seu sobre nome: ");
    fgets(sobrenome, sizeof(sobrenome), stdin);
    sobrenome[strcspn(sobrenome, "\n")] = '\0';
    printf("Sobrenome: %s\n", sobrenome);
    
    printf("Digite seu email: ");
    fgets(email, sizeof(email), stdin);
    email[strcspn(email, "\n")] = '\0';
    printf("Email: %s\n", email);
    
    printf("Digite seu numero de telefone: ");
    scanf("%d", &celular);
    printf("Celular: %d\n", celular);
    getchar();
    
    printf("Digite Sua data de nascimento: ");
    scanf("%d", &datanascimento);
    printf("Data de nascimento %d\n", datanascimento);
    getchar();
    return 0; 
    
    
    
}    
