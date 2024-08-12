#ejercicio 1
numeros = [1,2,4,5,5,4]
def elementos_repetidos(lista):
    for x in range(len(lista)):
        if lista.count(lista[x]) > 1:
            print('hay elementos repetidos')
            break
        else:
            print('no hay elementos repetidos')
#elementos_repetidos(numeros)

#ejercicio 2

oracion = ['las', 'rosas', 'son', 'rojas']

def vocales(oracion):
    voc = 0
    for x in range(len(oracion)):
        voc += oracion[x].count('a')
        voc += oracion[x].count('e')
        voc += oracion[x].count('i')
        voc += oracion[x].count('o')
        voc += oracion[x].count('u')
        
        if voc >= 2:
            print(oracion[x])
#vocales(oracion)


#ejercicio 3

iguales1 = [1,2,3]
iguales2 = [1,3,4]

def iguales(lista1, lista2):
    if lista1 > lista2:
        
        for x in range(len(lista2)):
            igual = lista1 + lista2
            
            if igual.count(lista2[x]) >= 2:
                print(lista2[x])
    else:
        for x in range(len(lista1)):
            igual = lista1 + lista2
            
            if igual.count(lista1[x]) >= 2:
                print(lista1[x])

            
#iguales(iguales1, iguales2)



#ejercicio 4
promed =[1,2,3,4]
def promedio(lista):
    s = 0
    for x in range(len(lista)):
        s += lista[x]

    p = s/len(lista)
    print(p)
promedio(promed)
  
#ejercicio5




        

    