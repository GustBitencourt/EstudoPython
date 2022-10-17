# Programa de pedra papel e tesoura

from random import randint

print('''
OPÇÔES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Escolha a opção: '))
computador = randint(0, 2)

pcEscolha = jogadas[computador]
jogadorEscolha = jogadas[jogador]

print('-=' * 30)
print('Jogador jogou: {}'.format(jogadorEscolha))
print('Computador jogou: {}'.format(pcEscolha))
print('-=' * 30)

if jogador == 0: #pedra
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('DERROTA')
    elif computador == 2:
        print('VITÓRIA')
elif jogador == 1: #papel
    if computador == 0:
        print('VITÓRIA')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('DERROTA')
elif jogador == 2: #tesoura
    if computador == 0:
        print('DERROTA')
    elif computador == 1:
        print('VITÓRIA')
    elif computador == 2:
        print('EMPATE')
else:
    print('Opção inexistente')


