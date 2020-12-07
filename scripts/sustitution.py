#importacion de modulos
import string

#definicion de constantes:  BUSCAR Y REEMPLAZAR : CONTROL + H
ALFABETO = string.ascii_uppercase

#RECUPERANDO CLAVE
clave = 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
clave = clave.upper()


print (ALFABETO)
print (clave)

#leemos el plaintext
plaintext = input("introduzca una palabra a encriptar")
print (plaintext)



ciphertext = ""
for letra  in plaintext:
    #algoritmo de transformacion
    index = ALFABETO.find(letra.upper())
    if index >= 0:
        if letra.isupper():
            letra = clave[index]
        else:
            letra = clave[index].lower()
    ciphertext += letra
    
    
print ("el texto cifrado es: {}" .format(ciphertext))