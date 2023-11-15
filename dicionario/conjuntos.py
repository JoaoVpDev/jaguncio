#conjuntos nao tem numeros repetidos e ja desordenados(nao estao sempre na mesma ordem), o importante [e o que tem la dentro
#nao e possivel modificar valores

meu_conjunto = {1,2,3,3,4,4,5}
print(meu_conjunto)

for i in meu_conjunto:
    print(i)

# subconjunto: 
conjunto1= {1,2,3}
conjunto2= {1,2,3,4,5}

print(conjunto1 < conjunto2) # conjunto 1 esta contido em b


conjunto3 = conjunto1.union(conjunto2) #uniao
print(conjunto3)

conjunto4 = conjunto1.intersection(conjunto2) #interseccao
print(conjunto4)

conjunto5 = conjunto2. difference(conjunto1) #diferenca entre conjunto 2 e o 1
print(conjunto5)

#atribuicao de uniao