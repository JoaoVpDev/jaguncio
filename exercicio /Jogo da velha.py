# Fac¸a um programa para determinar a proxima jogada em um Jogo da Velha. Assumir que ´
# o tabuleiro e representado por uma matriz de 3 x 3, onde cada posic¸ ´ ao representa uma ˜
# das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
# respectivamente uma casa contendo uma pec¸a minha (-1), uma casa vazia do tabuleiro
# (0), e uma casa contendo uma pec¸a do meu oponente (1).

matriz = [[0] * 3 for k in range(3)]

for linha in matriz:
    print(linha)

m1 = (0, 0)
m2 = [0, 1]
m3 = [0, 2]
m4 = [1, 0]
m5 = [1, 1]
m6 = [1, 2]
m7 = [2, 0]
m8 = [2, 1]
m9 = [2, 2]
posicoes = [m1, m2, m3, m4, m5, m6, m7, m8, m9]


for jogo in range(9): 
       
    if jogo % 2 == 0:
        print('Jogador 1, Escolhe sua casa. ',end='')
        posicao = int(input('Digite uma casa entre 1 e 9: ')) #usuario escolheu a posica
        while posicao < 1 or posicao > 9:
            print('Erro, digite um valora valido. ')
            posicao = int(input('Digite uma casa entre 1 e 9: ')) #usuario escolheu a posica

        posicao = posicoes[posicao - 1]
        matriz[posicao[0]][posicao[1]] = 1           #agora term que agregar um valor a tal possicao
        for linha in matriz:
            print(linha)
    else:
        print('Jogador 2, escolha sua casa. ', end='')
        posicao = int(input('Digite uma casa entre 1 e 9: ')) #usuario escolheu a posica
        while posicao < 1 or posicao > 9:
            print('Erro, digite um valora valido. ')
            posicao = int(input('Digite uma casa entre 1 e 9: ')) #usuario escolheu a posica

        posicao = posicoes[posicao - 1]
        matriz[posicao[0]][posicao[1]] = -1           #agora tem que agregar um valor a tal possicao
        for linha in matriz:
            print(linha)        


