def jogar():

    import random

    print("Bem vindo ao jogo da adivinhação!")
    nivel = int(input("Para:\n1- Facil\n2- Médio\n3- Dificil\nEscolha um nível: "))

    numero_secreto = random.randint(1, 100)
    tentativa_atual = 0
    pontos = 1000

    if nivel == 1:
        tentativas_total = 20
    elif nivel == 2:
        tentativas_total = 10
    elif nivel == 3:
        tentativas_total = 5
    else:
        print("Nível escolhido inválido!")
        tentativas_total = -1

    for rodada in range(1, tentativas_total + 1):

        chute = int(input("Escolha um número entre 1 e 100: "))
        tentativa_atual = tentativa_atual + 1
        print("Tentativa {} de {}:".format(tentativa_atual, tentativas_total), chute)

        if chute < 1 or chute > 100:
            print("Chute fora do intervalo informado!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou, seu chute foi maior que o número correto.")
                pontos = pontos - chute + numero_secreto
            elif menor:
                print("Você errou, seu chute foi menor que o número correto.")
                pontos = pontos - chute - numero_secreto

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
