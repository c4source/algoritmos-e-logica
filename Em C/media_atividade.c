

#include <stdio.h> 
//Funçao que calcula a media 
float calcular_media(float n1, float n2){
    return (n1 + n2) / 2.0f; 
 
}

int main(){
    // variaveis 
   
    float n1, n2, media;
    char escolha;
    // Dentro do loop parte de leitura
    do {printf("Digite a primeira nota: "); //Le a primeira nota
    scanf("%f", &n1);
    printf("Digite a segunda nota: ");
    scanf("%f", &n2);
    //A media recebe o valor do calculo da funçao    
    media = calcular_media(n1, n2); 
    printf ("A media do aluno e: %.2f\n", media); //Mostra a media 
    
    printf("Deseja calcular outra media [s/n]: ");  //Pergunta se ele quer fazer novamente
    scanf(" %c", &escolha);

    } while (escolha == 's' || escolha == 'S'); //Se a escolha for igual a s o loop repete o calculo da media
    
    printf("Programanda Encerrado. Volte sempre \n"); 
    
    return 0;
       
}
    


