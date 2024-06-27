# Crear un programa en python que permita ingresar al usuario 5 capitales (clave), que Ud. elija, con sus respectivos países 
# (valor) en un diccionario de datos. Una vez ingresado lo anterior, deberá solicitar el nombre de un turista y su capital de procedencia.
#  Para finalizar, con todos los datos previamenta ingresados, el programa deberá completar el texto con el siguiente formato: 
# "El turista con nombre XXXXX viene de la capital YYYYY y su país es ZZZZZZ"

datos={}
datos_turista={}

for x in range(5):
    capital=input("Ingrese una capital: ")
    print("")
    pais=input("Ingrese el pais de la capital: ")
    print("")
    datos[capital]=pais
for x in range(5): 
    turista=input("Ingrese el nombre de un turista:")
    print("")
    capi=input("De que capital es el turista:")
    print("")
    datos_turista[turista]=capi

for x in datos_turista:
    capi= datos_turista[x]
    capital = capi
    print("El turista con nombre ",x,"viene de la capital",capital,"y su pais es",datos[capital])
