from math import trunc
# moste o número inteiro apenas de um número
num = float(input('Type a number '))
print('O numero inserido {} inteiro é apenas {} mas podemos fazer apenas com int {}'.format(num, trunc(num), int(num)))