
def paredeArea(largura, altura):
    return  largura * altura 

def main():
    
    largura = float(input("Largura da parede: "))
    altura  = float(input("Altura da parede: "))
    area = paredeArea(largura, altura)
    tinta = area / 2  
    print(f"Area da parede: {area:.2f}, necessários {tinta:.2f} Litros de tinta para pinta-la")
    
       




if __name__ == "__main__":
    main()    
