# programa recebe duas entradas como notas de aluno
# retorna a média

nota1 = float(input('Nota primeiro semestre'))
nota2 = float(input('Nota segundo semestre'))

media = (nota1 + nota2) / 2

if media < 5:
    print('Média igual a {:.2f}, você está reprovado.'.format(media))
elif media < 7:
    print('Média igual a {:.2f}, você está de recuperação.'.format(media))
else:
    print('Média igual a {:.2f}, você está aprovado curta suas férias')