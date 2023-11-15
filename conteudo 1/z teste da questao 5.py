# Inicialização das variáveis
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0
moeda1 = moeda50 = moeda25 = moeda10 = moeda05 = centavo = 0

# Entrada do valor de saque
saque = float(input('Informe o valor de saque: '))

# Verificação de valor inválido

    # Processamento
    # Converter o valor para centavos (inteiro)
saque_centavos = int(saque * 100)

    # Notas
nota100 = saque_centavos // 10000
saque_centavos %= 10000

nota50 = saque_centavos // 5000
saque_centavos %= 5000

nota20 = saque_centavos // 2000
saque_centavos %= 2000

nota10 = saque_centavos // 1000
saque_centavos %= 1000

nota5 = saque_centavos // 500
saque_centavos %= 500

nota2 = saque_centavos // 200
saque_centavos %= 200

    # Moedas
moeda1 = saque_centavos // 100
saque_centavos %= 100

moeda50 = saque_centavos // 50
saque_centavos %= 50

moeda25 = saque_centavos // 25
saque_centavos %= 25

moeda10 = saque_centavos // 10
saque_centavos %= 10

moeda05 = saque_centavos // 5
saque_centavos %= 5

centavo = saque_centavos

 # Saída
print('NOTAS:')
print(f'{nota100} nota(s) de R$ 100.00')
print(f'{nota50} nota(s) de R$ 50.00')
print(f'{nota20} nota(s) de R$ 20.00')
print(f'{nota10} nota(s) de R$ 10.00')
print(f'{nota5} nota(s) de R$ 5.00')
print(f'{nota2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1} moeda(s) de R$ 1.00')
print(f'{moeda50} moeda(s) de R$ 0.50')
print(f'{moeda25} moeda(s) de R$ 0.25')
print(f'{moeda10} moeda(s) de R$ 0.10')
print(f'{moeda05} moeda(s) de R$ 0.05')
print(f'{centavo} moeda(s) de R$ 0.01')