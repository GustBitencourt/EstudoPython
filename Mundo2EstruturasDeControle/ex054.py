# ler o nasicmento de 7 pessoas, mostrar quantas não são maiores de idade e quantas ja possume masi de 18
from datetime import date

atual = date.today().year
maior = 0
menor = 0

for pessoa in range(1, 8):
    nascimento = int(input('Ano de nascimento {}: '.format(pessoa)))
    idade = atual - nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Há {} MAIORES de idade e {} MENORES de idade'.format(maior, menor))