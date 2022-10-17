# classifique atletas a partir do ano de seu nascimento
# até 9 - mirim, 14 infantil, 19 junior, 25 senior, mais master

from datetime import date

atual = date.today().year
anoNascimento = int(input('Ano de nascimento: '))
idade = atual - anoNascimento

if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')