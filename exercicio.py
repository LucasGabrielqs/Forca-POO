lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

def maior_valor():
    maior = 0
    for index in range(0, len(lista)):
        if (maior < lista[index]):
            maior = lista[index]
    print("O maior valor da lista é {}".format(maior))
def menor_valor():
    menor = lista[0]
    for index in range(0,len(lista)):
        if (menor > lista[index]):
            menor = lista[index]

    print("O menor valor é {}".format(menor))

def numeros_pares():
    numeros_pares = []
    for index in range(0, len(lista)):
        if (lista[index] % 2 == 0):
            numeros_pares.append(lista[index])
    print(" Os numeros pares da lista são: {}".format(numeros_pares))

def encontrar_primeiro_elemento():
    elemento = lista[0]
    quantidade_repeticoes = 0
    for index in range(0,len(lista)):
        if (lista[index] == elemento):
            quantidade_repeticoes +=1
    print("A quantidade de vezes que o {} se repete na lista é {}".format(elemento,quantidade_repeticoes))

def media_dos_elementos():
    media = 0
    soma_elementos = 0
    for index in range(0,len(lista)):
        soma_elementos = (soma_elementos + lista[index])
    media = soma_elementos/len(lista)
    print("A media dos elementos da lista é {}".format(media))

def soma_dos_elementos_negativos():
    soma_valores_negativos = 0
    for index in range(0, len(lista)):
        if (lista[index] < 0 ):
            soma_valores_negativos = soma_valores_negativos + lista[index]
    print("A soma dos valores negativos é {}".format(soma_valores_negativos))

soma_dos_elementos_negativos()