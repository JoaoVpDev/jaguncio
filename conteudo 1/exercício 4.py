# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 
# 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
# para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
import math
ordem_a = 80000
crescimento_a = 1.03

ordem_b = 200000
crescimento_b = 1.015
contador = 0

while ordem_b >= ordem_a:
    ordem_a = ordem_a *  crescimento_a
    contador += 1
    ordem_b = ordem_b *crescimento_b
print(math.trunc(ordem_a))
print(math.trunc(ordem_b))
print(f'Demorou {contador} anos para a população A se igualar a população B ')