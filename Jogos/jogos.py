import forca
import adivinhacao


def escolha_jogo():
    print('********************************')
    print('****\033[1;30mEscolha o jogo desejado!\033[m****')
    print('********************************')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print('Jogando forca.')
        forca.jogar()
    elif (jogo == 2):
        print('jogando adivinhação.')
        adivinhacao.jogar()
if(__name__=='__main__'):
    escolha_jogo()