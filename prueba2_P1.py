# Crear un programa en python que permita al usuario ingresar N notas en una lista. 
# Para finalizar deberá ingresar un 0. Una vez finalizado, deberá mostrar lo siguiente: 
# 1) Cantidad de notas 
# 2) Promedio de notas 
# 3) Cantidad de notas bajo nota 4,0
# 4) Cantidad de notas igual o mayor que nota 4,0

notas=[]
total=0
while True:
    nota=float(input("Ingrese la nota(para salir ingrese 0): "))
    if nota == 0:
        break
    notas.append(nota)
cont=0
altas=0
bajas=0
for x in notas:
    total=x+x
    if x >= 4.0:
        altas=altas+1
    elif x < 4.0:
        bajas=bajas+1
    cont=cont+1
    
prom = total/cont

print("Cantidad de notas:",cont,"\nPromedio de notas:",prom,"\nCantidad de notas bajo 4,0:",bajas,"\nCantidad de notas igual o mayor que 4,0:",altas)


