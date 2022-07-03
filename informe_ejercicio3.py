archivo=open("Empleado.dat","r")

cod_empleado=[]
sueldo_empleado=[]
nom_apellido=[]
cat=[]
categoria={1:"Mecanico",2:"conductor"}
cont=0
lista=archivo.readline()
lineas=lista.split(",")
while lineas=="":
    lineas=lista.split(",")
    cont=cont+1
    lista1=int(lineas[0])
    cod_empleado.append(lista1)
    lista2=float(lineas[1])
    sueldo_empleado.append(lista2)
    lista3=lineas[2]
    nom_apellido.append(lista3)
    lista4=int(lineas[3])
    cat.append(lista4)
    lista=archivo.readline()
archivo.close()

sumasuel=0
promedio=0
promec=0
suelmec=0
contmec=0

for x in range(cont):
    sumasuel=sumasuel+sueldo_empleado[x]
    if cat[x]==1:
        contmec=contmec+1
        suelmec=suelmec+sueldo_empleado[x]

print(cont)
promedio=sumasuel//cont
promec=suelmec//contmec


print("El padron queda conformado de la siguiente manera")
for x in range(cont):
    print(cod_empleado[x],nom_apellido[x],sueldo_empleado[x])
    print("Categoria: ",categoria[cat[x]])

print("///////////////////////////////////////")
print("La cantidad de empleados es de: ",cont)
print("///////////////////////////////////////")
print("El promedio de los suedos es: ",promedio)
print("")
if contmec>=1:
    print("El promedio de los sueldos de los mecanicos es: ",promec)