lista=[2,4,3,1,5]
def media(lista):
    
    supapa =[None]*(len(lista))
    for i in range(10):
        p = min(lista)
        supapa[i] = p
        lista.remove(p)
        if lista ==[]:
            break
    me =len(supapa)
    me = me/2

    print('las lista ordenada  es:', supapa)
    print('la mediana es:', supapa[int(me)])

media(lista)