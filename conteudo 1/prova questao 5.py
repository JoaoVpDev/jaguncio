#entrada
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0
moeda1 = moeda50 = moeda25 = moeda10 = moeda05 = centavo = 0

saque = float(input(''))

#processamento
#notas

saque *= 100 #tem que multiplicar por 100, pois a divis'ao por decimal nao e precisa
nota100 = int(saque // 10000)
saque -= nota100 * 10000

nota50 = int(saque // 5000)
saque -= nota50 * 5000

nota20 = int(saque // 2000)
saque -= nota20 * 2000

nota10 = int(saque // 1000)
saque -= nota10 * 1000

nota5 = int(saque // 500)
saque -= nota5 * 500

nota2 = int(saque // 200)
saque -= nota2 * 200

#moedas
moeda1 = int(saque // 100)
saque -= moeda1 * 100

moeda50 = int(saque // 50)
saque -= moeda50 * 50

moeda25 = int(saque // 25)
saque -= moeda25 * 25

moeda10 = int(saque // 10)
saque -= moeda10 * 10

moeda05 = int(saque // 5)
saque -= moeda05 * 5

centavo = int(saque)

#saida
print('NOTAS:')
print(f'{nota100}  nota(s) de R$ 100.00')
print(f'{nota50}  nota(s) de R$ 50.00')
print(f'{nota20}  nota(s) de R$ 20.00')
print(f'{nota10}  nota(s) de R$ 10.00')
print(f'{nota5}  nota(s) de R$ 5.00')
print(f'{nota2}  nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1}  moeda(s) de R$ 1.00')
print(f'{moeda50}  moeda(s) de R$ 0.50')
print(f'{moeda25}  moeda(s) de R$ 0.25')
print(f'{moeda10}  moeda(s) de R$ 0.10')
print(f'{moeda05}  moeda(s) de R$ 0.05')
print(f'{centavo}  moeda(s) de R$ 0.01')
