#importacion de librerias

#constantes


#funciones y metodos

def es_primo(numero):
    for n in range (2,numero,1):                         
        if numero % n == 0:        
            return False      
    return True 

#mi programa principal 

if __name__ == "__main__":
    #ingreso de numero por teclado
    numero= int(input("ingrese un numero"))


    #imprimo segun validacion
    if es_primo(numero):
        print(f"el numero: {numero} es primo")
    else:
        print(f"el numero: {numero} NO es primo")