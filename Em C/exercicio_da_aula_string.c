#include <stdio.h>
#include <string.h> 
int main(){
    
    char nome[51];
    char sobrenome[51];
    char email[51];
    char datanascimento[10], celular[16];
    
    printf("Digite seu nome: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0';
     
    
    //funçao Fgets para ler string --> + seguro 
    printf("Digite seu sobrenome: ");
    fgets(sobrenome, sizeof(sobrenome), stdin);
    sobrenome[strcspn(sobrenome, "\n")] = '\0';
   
    
    printf("Digite seu email: ");
    fgets(email, sizeof(email), stdin);
    email[strcspn(email, "\n")] = '\0';
    
    
    printf("Digite seu numero de telefone: ");
    fgets(celular, sizeof(celular), stdin);
    celular[strcspn(email, "\n")] = '\0'; 
    
    
    
    printf("Digite Sua data de nascimento: ");
    fgets(datanascimento, sizeof(datanascimento), stdin); 
    datanascimento[strcspn(datanascimento, "\n")] = '\0';

    
    printf("=== Lista de dados ===\n");
    strcat(nome, " ");
    strcat(nome, sobrenome);
    printf("Nome: %s\n", nome);
    printf("Sobrenome: %s\n", sobrenome);
    printf("Email: %s\n", email);
    printf("Data de nascimento %s\n", datanascimento);
    
    return 0;
        
}    
