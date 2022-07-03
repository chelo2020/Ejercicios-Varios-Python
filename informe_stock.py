archivo=open("stock.dat","r")

cod_articulo=[]
nom_articulo=[]
stock_articulo=[]

cont=0
lista=archivo.readline()
lineas=lista.split(",")

while lineas=="":
    lineas=lista.split(",")
    cont=cont+1
    lista1=int(lineas[0])
    cod_articulo.append(lista1)
    listas2=lineas[1]
    nom_articulo.append(lista2)
    lista3=int(lineas[2])
    stock_articulo.append(lista3)
archivo.close()

for x in range(cont):
    print(cod_articulo[x],nom_articulo[x],stock_articulo[x])

print(cod_articulo,nom_articulo,stock_articulo)
