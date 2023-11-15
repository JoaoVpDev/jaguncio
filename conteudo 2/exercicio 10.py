# leitura da string 
s = input()

# encontra a posição do meio da string
# sempre lembrando que inicia na posição zero 
meio = int(len(s)/2)

s1 = s[0:meio:]    # a primeira parte da string
s1 = s1[::-1]      # ...agora invertida

# exibe a primeira parte da string in5vertida
# e o restante sem modificações
print(s1 + s[meio:])
