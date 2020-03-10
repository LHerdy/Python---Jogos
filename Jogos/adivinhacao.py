import random

def jogar():
    print('**************************')
    print('****Bem vindo ao jogo!****')
    print('**************************')

    numero_secreto = random.randrange(0, 11)
    total_de_tentativas = 0
    pontos = 100
    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if( nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    elif(nivel == 3):
        total_de_tentativas = 3
    else:
        print('Você digitou o nível errado, tente novamente!')


    for rodada in range (1, total_de_tentativas + 1):
        print(f'Tentativas {rodada} de {total_de_tentativas}')
        chute_str = input('Digite um número entre 1 e 10: ')
        print('Você digitou ', chute_str)

        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print('Você deve digitar um valor entre 1 e 10.')
            continue
        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute
        if (acertou):
            print(f'Você acertou! fez {pontos} pontos')
            break
        else:
            if(maior ):
                print('Você chutou para cima!')
            elif(menor):
                print('Você chutou para baixo')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print('FIM DO JOGO')

if(__name__=='__main__'):
    jogar()