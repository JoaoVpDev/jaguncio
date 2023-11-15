# escrever algoritimo para ler nome e notas de 30 alunos de uma turma, depois exibir uma lista dos alunos com nota maior que 7

alunos = [0] * 4
notas = [0] * 4

aprovados= []

for i in range(0, 4):
    alunos[i] = str(input('Nome do aluno: '))
    notas[i] = int(input('Nota do aluno'))
    if notas[i] >= 7:
        aprovados.append(alunos[i])
        
print(f'os aluno com nota maior que 7 sao: {aprovados}')