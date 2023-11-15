# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Digite um numero: '))
fatorial = 1
for i in range(num, 0, -1):
    fatorial = fatorial * i
    
#incomplto, sem print