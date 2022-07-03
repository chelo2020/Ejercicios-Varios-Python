archivo=open("ventas.dat","r")

cod_ventas=[]
pro_vendedido=[]
cant_vendida=[]
cont=0

lista=archivo.readline()
lineas=lista.split(",")
while lineas=="":
    lineas=lista.split(",")
    cont=cont+1
    lista1=int(lineas[0])
    cod_ventas.append(lista1)
    lista2=(lineas[1])
    pro_vendedido.append(lista2)
    lista3=int(lineas[2])
    cant_vendida.append(lista3)
archivo.close()

print("##########################################")
print("Los productos vendidos son: ",pro_vendedido)
print("##########################################")
print("Las cantidades vendidas son: ",cant_vendida)

for x in range(cont):
    print("##########################################")
    print(cod_ventas[x],pro_vendedido[x],cant_vendida[x])
