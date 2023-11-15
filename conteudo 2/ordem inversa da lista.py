# Fazer um algoritimo para ler um vetor de 8 numeros inteiros e imprimirna tela os conteudo do vetor lido(mesma ordem)
#bonus: altere a ordem 
#bonus 2: coloque a soma dos valores da lista e mostre se [e numero positivo ou negativo]

valores = [0] * 8
for i in range(-1, -9, -1):
    valores[i] = int(input('Digite um valor: '))

soma = sum(valores)
print(f'a soma e dos valores da lista e : {soma}')
if soma > 0:
    print('A soma dos numero e positiva')
else:
    print('negativo')
print(valores)