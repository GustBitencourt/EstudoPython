# programa que continue pedido a resposta ao usuário enquanto ele não acerta o número entre 1 e 10
from random import randint
sorteio = randint(1,10)

rightAnswer = int(input('Digite um número entre 1 e 10 '))

while rightAnswer != sorteio:
    print('Errado, tente até acertar')
    rightAnswer = int(input('Digite um número entre 1 e 10 '))

print('Acertou o número era o {}.'.format(rightAnswer))

print('\n=========Exemplo Guanabara=============')

print('Sorteando o número')
computador = randint(1, 10)
acertou = False
while not acertou:
    jogador = int(input('Digite um número entre 1 e 10 '))
    if jogador == computador:
        acertou = True

print('Acertou Mizeravi')