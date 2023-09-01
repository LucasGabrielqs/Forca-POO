import random
print("*******************")
print("***Jogo da Forca***")
print("*******************")
letras_acertadas=[]
acertou = False
enforcou = False
def categoria_palavra():
    global palavra_secreta
    escolha_palavra_secreta = {"frutas":["banana" , "maca"], "animais":["cachorro","gato"], "estados_brasil":["ceara","bahia"]}
    print("Escolha a categoria da palavra secreta")
    print("1 - Frutas")
    print("2 - Animais")
    print("3 - Estados do Brasil")
    opcao = int(input())
    match opcao:
        case 1:
            palavra_secreta = random.choice(escolha_palavra_secreta["frutas"])
        case 2:
            palavra_secreta = random.choice(escolha_palavra_secreta["animais"])
        case 3:
            palavra_secreta = random.choice(escolha_palavra_secreta["estados_brasil"])
    return palavra_secreta

def criar_lista_letras_acertadas():
    for index in range(0, len(palavra_secreta)):
        letras_acertadas.append("_")

def dicas_palavra_secreta():
    global dica_jogo
    dica = {"banana" : "Amarela e Curva", "maca" : "Arredonda e Vermelha", 
            "gato" : "as vezes te ama as vezes não", "cachorro" : "Melhor amigo do homem" , 
            "ceara" : "quente e famoso pela população ter a cabeça grande", "bahia" : "Conhecido pela população so dormir"}
    dica_jogo = dica[palavra_secreta]
    print(dica_jogo)
    return dica_jogo

def nivel_dificuldade():
    global tentativas
    print("Escolha o Nivel de dificulade")
    print("1 - Facil")
    print("2 - Mediana")
    print("3 - Dificil")
    opcao_nivel_dificuldade = int(input())     
    match opcao_nivel_dificuldade:
        case 1:
            tentativas = 10
        case 2:
            tentativas = 5
        case 3:
            tentativas = 3
    return tentativas
    

def regra_adcional(chute):
    global tentativas
    teste = False
    vogais = ['a','e','i','o','u']
    for i in range(0, len(vogais)):
        if (chute == vogais[i]):
            tentativas += 1

def registro_de_jogadores(nome_jogador):
    jogadores = [{'nome' : 'Lucas','pontuacao': 100}]
    
    # lista_nome = []
    # lista_pontuacao = []
    # for i in range(0, len(lista_nome)):
    #     if (nome_jogador != lista_nome[i]):
    #         lista_nome.append(nome_jogador)
    #         lista_pontuacao.append(tentativas)
    #     else:
    #         lista_pontuacao[i] += tentativas    
    # for index in range(0, len(lista_nome)):
    #     print("Nome do Jogador {} sua pontuação {}".format(lista_nome[index],lista_pontuacao[index]))


print("Digite o nome do jogador")
nome_jogador = input()
nivel_dificuldade()
categoria_palavra()
criar_lista_letras_acertadas()

while (not acertou and tentativas>0):
    dicas_palavra_secreta()
    chute = input("Digite uma letra:")
    if (chute in palavra_secreta):
        posicao = 0
        teste = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posição {}'.format(letra, posicao))
                letras_acertadas[posicao] = letra
                if (teste == 0):
                    regra_adcional(chute)
                    teste += 1  
            posicao += 1
    else:
        tentativas -= 1
        print(tentativas)    
    acertou = '_' not in letras_acertadas

    print(letras_acertadas)

if (acertou):
    registro_de_jogadores(nome_jogador)
    print("Você Ganhou!!!")
else:
    print("Você Perdeu!!!")
    print("A palavra secreta era ", palavra_secreta)

print("Fim de Jogo")