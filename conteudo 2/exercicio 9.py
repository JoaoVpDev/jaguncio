# Fazer um programa para ler 10 strings contendo números ou expressões aritméticas. Após ler os strings, faça o Python avaliar as expressões 
# e somar o resultado de todas as 10. Exiba o valor da soma ao final como ponto flutuante (float).

numeros = [(input()) for i in range(3)]
somas = 0
for i in range(3):
    somas += eval(numeros[i])

print(somas)
