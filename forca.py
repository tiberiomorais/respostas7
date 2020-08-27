import random

lista_frutas = ['uva','pera','cana','abacate','laranja','goiaba','umbu','banana','morango','siriguela'
                'abacaxi','acerola','amora','cacau','caqui','carambola','jaca','cereja','framboesa',
                'inga','caja','jambo','jenipapo','kiwi','limao','manga','macacuja','melancia','pequi',
                'pessego','pitanga','tamarindo','tangerina']

fruta_escolhida = random.choice(lista_frutas)
fruta_escolhida = fruta_escolhida.strip()

tentativas_max = 6
letras_digitadas = []
print(fruta_escolhida)
tamanho1 = len(fruta_escolhida)
tela1 = list('_' * tamanho1)


acertos = 0
erros = 0

print('\033[1;34m -' * 17)
print(' '*8,'\033[1;32m JOGO DA FORCA')
print('\033[1;34m -' * 17)
print(f'\033[1;90m DICA: O nome dessa fruta tem {len(fruta_escolhida)} letras')



def imprimir(erros):

    if erros == 1:
        print( '''\033[1;33m_____
                 \033[1;33m/     |
                 \033[1;33m|     0
                 \033[1;33m|
                 \033[1;33m|
                 \033[1;33m|''')
    elif erros == 2:
        print( '''\033[1;33m_____
                 \033[1;33m/     |
                 \033[1;33m|     0
                 \033[1;33m|     |  
                 \033[1;33m|
                 \033[1;33m|''')
    elif erros == 3:
        print( '''\033[1;33m_____
                \033[1;33m/     |
                \033[1;33m|     0
                \033[1;33m|    /|  
                \033[1;33m|    
                \033[1;33m| \033[1;33m''')
    elif erros == 4:
        print( '''\033[1;33m_____
                  \033[1;33m/    |
                  \033[1;33m|    0
                  \033[1;33m|   /|\  
                  \033[1;33m|    
                  \033[1;33m|\033[1;33m''')
    elif erros == 5:
        print( '''\033[1;33m_____
                 \033[1;33m/     |
                 \033[1;33m|     0
                 \033[1;33m|    /|\  
                 \033[1;33m|     |  
                 \033[1;33m|\033[1;33m''')
    elif erros == 6:
        print( '''\033[1;33m_____
                \033[1;33m/     |
                \033[1;33m|     0
                \033[1;33m|    /|\  
                \033[1;33m|     |  
                \033[1;33m|    /\033[1;33m''')
    elif erros == 7:
        print( '''\033[1;91m_____
                 \033[1;91m/     |
                 \033[1;91m|     0
                 \033[1;91m|    /|\  
                 \033[1;91m|     |  
                 \033[1;91m|    / \ \033[1;91m''')




while True:


    print('\n \033[0;0m', tela1)

    if '_' in tela1:
        if erros <= tentativas_max:
            letra = str(input(f'\n Informe a letra: '))

            if letra in fruta_escolhida:
                #qt_under = tela1.count('_')
                for n in range(0,tamanho1):
                    if letra == fruta_escolhida[n]:
                        tela1[n] = fruta_escolhida[n]

                #print(tela1)

            else:
                print('Você errou! Tente novamente.')
                erros += 1
                imprimir(erros)
        else:
            print('\033[1;91m GAME OVER')
            imprimir(erros)
            break
    else:
        print('\n \033[;1m, \033[1;32m C O N G R A T U L A T I O N S')
        print(f'A PALAVRA É: f{fruta_escolhida}')
        break

