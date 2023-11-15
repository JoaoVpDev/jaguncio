lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

#tupulas sao imutaveis

# lanche[1] = 'refrigerante' -> deu erro
# print(lanche[-3])

# for cont in range(0, len(lanche)):
#     print(lanche[cont])

# tanto faz o de cima ou o de baixo, os dois serao a mesma coisa

# for comida in lanche:
    # print(f'Eu vou comer {comida} na posicao{cont}') # na posicao{cont} mostra a posicao do elemento

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicao {pos}')
# print('comi pra caramba')

print(sorted(lanche)) #botar em ordem
print(lanche)