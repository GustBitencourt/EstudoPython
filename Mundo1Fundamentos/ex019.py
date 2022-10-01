from random import choice
# faça um sorteio entre os quatro nome inseridos

aluno1 = input('Digite o primeiro aluno ')
aluno2 = input('Digite o segundoo aluno ')
aluno3 = input('Digite o terceiro aluno ')
aluno4 = input('Digite o quarto aluno ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(listaAlunos)

print('O aluno escolhido foi {}'.format(escolhido))
