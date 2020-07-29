import random

def jogar():

    abertura()
    palavra_secreta = importa_palavra_secreta()
    lista_acertou = inicializa_letras_acertadas(palavra_secreta)
    print(lista_acertou)

    chances = 6
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute.upper() in palavra_secreta:
            marca_chute_correto(chute, lista_acertou, palavra_secreta)
        else:
            chances = chances - 1
            print("A palavra secreta não contém esta letra!\nVocê tem mais {} chances.".format(chances))

        print(lista_acertou)

        if chances == 0:
            enforcou = True
            derrota(palavra_secreta)
        if list(palavra_secreta) == lista_acertou:
            acertou = True
            vitoria()

#__________________________________________________________________________________________________________________

def abertura():
    print("*******************************")
    print("**Bem vindo ao jogo da forca!**")
    print("*******************************")

def importa_palavra_secreta():
    # Importa as a serem usadas no jogo
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, lista_acertou, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            print("Encontrei a letra {} na posição {}".format(letra, index))
            lista_acertou[index] = letra
        index += 1

def derrota(palavra_secreta):
    print("Você perdeu!")
    print("A palavra secreta é {}.".format(palavra_secreta.lower()))

def vitoria():
    print("Você acertou a palavra secreta!")

if(__name__ == "__main__"):
    jogar()