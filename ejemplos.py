#Crear y cargar por teclado en el bloque principal del 
#programa una lista de 5 enteros. Implementar una 
#función que imprima el mayor y el menor valor de la 
#lista.

def mayor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    print("El valor mayor de la lista es", mayor)
    print("El valor menor de la lista es", menor)          

                
# bloque principal

lista=[]
for x in range(3):
    valor=int(input("Ingrese un valor: "))
    lista.append(valor)
mayor(lista)
