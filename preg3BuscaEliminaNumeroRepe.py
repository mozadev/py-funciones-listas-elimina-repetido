lisNumeros=[]

cantNum=int(input("ingrese cantidad de numeros de la lista:"))
while cantNum<2:
    cantNum=int(input("tiene q ser mayor que 2 numeros:"))
for i in range(cantNum):
    numero=int(input("ingrese el numero ["+str(i)+"] : "))
    lisNumeros.append(numero)

print(lisNumeros)
valorBuscado=int(input("ingrese el valor buscado"))
def encontrarRepetidos(lisNumeros,valorBuscado):
    contador=0
    lisPosi=[]
    for i in range(len(lisNumeros)):
        if valorBuscado==lisNumeros[i]:
            contador+=1
            lisPosi.append(i)
    print("lista de de las posiciones donde se encontro el valor buscado")
    print(lisPosi)

    if contador>1:
        # x = 0
        # for j in lisPosi:
        #     aEliminar=lisNumeros[j-x]
        #     lisNumeros.remove(aEliminar)
        #     x=x+1
        lisNumeros=list(set(lisNumeros))



    print("lista de numeros sin repetir: ")
    print(lisNumeros)

encontrarRepetidos(lisNumeros,valorBuscado)
