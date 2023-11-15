# numero = (0, 1, 2, 3, 4)
# extenso = ('zero' ,'um' ,'dois' ,'tres' ,'quatro')

# resposta = int(input('digite um numero entre 0 e 4: '))

# if resposta >= 0 and resposta <= 4:
#         print(f' o seu numero e {extenso[resposta]}')

# while resposta < 0 or resposta > 4:
#     print('numero invalido, tente novamente')
#     resposta = int(input('digite um numero entre 0 e 4: '))
#     print(f' o seu numero e {extenso[resposta]}')

#correcao

cont = ('zero' ,'um' ,'dois' ,'tres' ,'quatro')
while True:
    num = int(input('Digite um numero entre 0 e 4: '))
    if 0 <= num <= 4:
        break
    print('Tente novamente. ', end='')
print(f'voce digitou o numero {cont[num]}')
    