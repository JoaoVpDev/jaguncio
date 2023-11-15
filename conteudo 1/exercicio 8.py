# Faça um programa que leia 5 números e informe a soma e a média dos números.
numero = []
soma = media = 0
for i in range(0, 5):
    num = int(input('digite um numero: '))
    numero.append(num)
    soma += num
media = soma / 5
    
print(f'A soma entre os numero e: {soma} e a media e: {media}')