# programa que recebe o ano de nasicmento como entradas
# retorna quando ele deveria se alistar, ou se passou

from datetime import date

atual = date.today().year
anoNascimento = int(input('Ano de nascimento: '))
idade = atual - anoNascimento

print('Pessoa nascida em {}, tem {} anos'.format(anoNascimento, idade))

if idade < 18:
    print('Você ainda tem {} anos para se alistar'.format(18 - idade))
elif idade >= 19:
    print('Você tem {} anos, deveria ter se alistado há {} anos, regularize sua situação'.format(idade, (idade - 18)))
else:
    print('Você tem {} anos. Se aliste imediatamente'.format(idade))

