# Crear un programa en python que permita al usuario ingresar 10 precios de productos en pesos chilenos en una lista. 
# Una vez finalizado, deberá convertir los 10 precios ingresados en pesos chilenos a valor en dólares USD (Valor USD/CLP hoy: $950) 
# modificando cada elemento de la lista a su respectivo valor en USD. Finalmente, mostrar la lista resultante.

lista=[]
lista_d=[]
for x in range(10):
    precio=int(input("Ingrese 10 precios de productos en peso chileno: $"))
    lista.append(precio)

for x in lista:
    dolar=x*1/950
    print ("precios: Peso chileno: $",x,"son en Dolar: $",dolar)

