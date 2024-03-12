import random
import time

def ordenaLista(lista):
    lista2 = sorted(lista, key = len)
    return lista2

def ordemAlfabetica(lista):
    return sorted(lista)

def juncaoListas(lista1, lista2):
    lista3 = []
    for a,b in zip(lista1, lista2):
        lista3.append(a)
        lista3.append(b)
    return lista3

def retornaPar (lista):
    lista2 = []
    for i in range(len(lista)):
        if i%2 == 0:
            lista2.append(lista[i])
        else:
            pass
    return lista2

def ordemAlfabetica(lista):
    sorted(lista)
    return lista

def imparOuPar (lista):
    listaImpar = []
    listaPar = []
    for i in lista:
        if i % 2 == 0:
            listaPar.append(i)
        else:
            listaImpar.append(i)
    return listaImpar, listaPar

def encontrarMaiores(lista):
    maiorGeral = float('-inf')
    for sublist in lista:
        if sublist:
            maiorSublista = max(sublist)
            print("Maior número na sublista:", maiorSublista)
            if maiorSublista > maiorGeral:
                maiorGeral = maiorSublista
    
    print("Maior número no geral:", maiorGeral)

def calcularMedia(lista):
    listaComMedia = []
    totalValores = 0
    totalNumeros = 0

    for sublist in lista:
        soma = sum(sublist)
        media = soma / len(sublist)
        sublist.append(media)
        totalValores += soma
        totalNumeros += len(sublist) - 1

        listaComMedia.append(sublist)

    mediaGeral = totalValores / totalNumeros
    listaGeral = [mediaGeral]

    listaGeral.extend([sum(item) / len(item) for item in zip(*lista)])

    listaComMedia.append(listaGeral)

    return listaComMedia

def removeNumeros(lista):
    novaLista = lista[4:-4]
    return novaLista

def removeNumeros(lista):
    novaLista = lista[1:-1]
    return novaLista

def ehOrdenada(lista):
    listaOrdenada = sorted(lista)
    if lista == listaOrdenada:
        return True
    else:
        return False
    
def temNumeroIguais(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
    return False
        
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5, 1]
lista3 = [1, 2, 3, 4, 5, 5]

def colocaNumeros(p):
    lista = []
    for i in range(p):
        parametro = random.randint(1, p)
        lista.append(parametro)
    return lista

def busca(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return None

def buscaBinaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    for i in range(len(lista)):
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None
