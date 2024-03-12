import random
import time
from todasFuncoes import *

menu = '''

Seja Bem-Vindo
0 - Sair
1 - Retorna uma nova lista contendo o seu conteúdo em ordem crescente (segundo a quantidade de caracteres).
2 - Retorna o seu conteúdo em ordem alfabética.
3 - Retorna uma terceira lista que tenha os conteúdos das duas de forma alternada.
4 - Retorna somente os valores das posições pares desta lista.
5 - Retorna os seus valores em ordem alfabética.
6 - Colocar todos estes valores em duas listas: uma somente de números pares e uma somente com os números ímpares.
7 - Função que recebe uma lista ne numeros inteiros e imprime o maior número existente em cada uma das listas internas e o maior número no geral.
8 - Retorna o valor da media de cada uma de suas listas internas inserindo-os ao fim de cada uma delas.
9 - Retorne uma nova lista com todos os elementos originais, exceto os 4 primeiros e os 4 últimos.
10 - Remova o primeiro e o último elemento da lista.
11 - Função que recebe uma lista como parâmetro e retorne True caso a lista esteja ordenada de forma crescente e False caso contrário.
12 - Função que recebe uma lista como parâmetro e retorne True caso haja algum elemento que apareça mais de uma vez e False caso contrário.
13 - Retorna uma lista de inteiros preenchida de forma aleatória de acordo com a quantidade especificada no parâmetro.
14 - Diferenca entre uma busca normal e uma busca binaria

'''

print(menu)
while True:
    pergunta = int(input('Escolha umas das opcoes: '))
    if pergunta == 0:
        print('Tchau')
        break
    elif pergunta == 1:

        lista = ['carro', 'moto', 'bicicleta']
        print(ordenaLista(lista))
        
    elif pergunta == 2:

        lista = ['carro', 'moto', 'bicicleta']
        print(ordemAlfabetica(lista))

    elif pergunta == 3:

        lista1 = ['carro', 'moto', 'bicicleta']
        lista2 = ['1', '2', '3']
        print(juncaoListas(lista1, lista2))

    elif pergunta == 4:

        lista = [3,6,1,9,10]
        print(retornaPar(lista))

    elif pergunta == 5:

        lista = ['b', 'c', 'y', 'k']
        print(ordemAlfabetica(lista))

    elif pergunta == 6:

        lista = []
        i = 0
        while i < 10:
            numero = int(input('Digite um valor real: '))
            lista.append(numero)
            i = i + 1

        print(imparOuPar(lista))

    elif pergunta == 7:

        listaDeListas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        encontrarMaiores(listaDeListas)

    elif pergunta == 8:

        listaDeListas = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
        listaComMedia = calcularMedia(listaDeListas)
        print(listaComMedia)

    elif pergunta == 9:

        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        print(removeNumeros(lista))

    elif pergunta == 10:

        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        print(removeNumeros(lista))

    elif pergunta == 11:

        lista = [8,5,9,3,1,0,5,34]
        print(ehOrdenada(lista))
        lista = [1,2,3,4,5]
        print(ehOrdenada(lista))

    elif pergunta == 12:

        lista1 = [1, 2, 3, 4, 5]
        lista2 = [1, 2, 3, 4, 5, 1]
        lista3 = [1, 2, 3, 4, 5, 5]

        print(temNumeroIguais(lista1)) 
        print(temNumeroIguais(lista2))  
        print(temNumeroIguais(lista3))

    elif pergunta == 13:

        parametroEscolhido = int(input('Digite a quantidade de numeros que desejar para uma lista: '))
        print(colocaNumeros(parametroEscolhido))

    elif pergunta == 14:

        listaDeValores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        print(listaDeValores)
        valor1 = int(input('Digite um valor alvo para a busca: '))
        indice = busca(listaDeValores, valor1)
        if indice is not None:
            print(f'O valor {valor1} está na posição {indice} da lista.')
        else:
            print(f'O valor {valor1} não está na lista.')

        listaDeValores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        print(listaDeValores)
        valor2 = int(input('Digite um valor alvo para a busca: '))
        indice = busca(listaDeValores, valor2)
        if indice is not None:
            print(f'O valor {valor2} está na posição {indice} da lista.')
        else:
            print(f'O valor {valor2} não está na lista.')

        listaGigante = [random.randint(1, 1000000) for i in range(1000000)]

        valor = int(input('Digite o valor a ser buscado: '))

        inicio = time.time()
        indice = busca(listaGigante, valor)
        if indice is not None:
            print(f'O valor {valor} está na posição {indice} da lista.')
        else:
            print(f'O valor {valor} não está na lista.')
        fim = time.time()
        tempoCorrido = fim - inicio
        print('Tempo corrido para a finalizacao utilizando a busca normal em segundos: ', tempoCorrido)

        inicio = time.time()
        indice = buscaBinaria(sorted(listaGigante), valor)
        if indice is not None:
            print(f'O valor {valor} está na posição {indice} da lista.')
        else:
            print(f'O valor {valor} não está na lista.')
        fim = time.time()
        tempoCorrido = fim - inicio
        print('Tempo corrido para a finalizacao utilizando a busca binaria em segundos: ', tempoCorrido)

    else:
        print('Opcao inexistente')
