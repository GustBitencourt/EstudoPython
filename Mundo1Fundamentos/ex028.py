# programa que sorteia um numero entre 0 e 5, verifique se é o mesmo inserido pelo usuário

from random import randint

userNumber = int(input('Type a number between 0 and 5 '))
drawNumber = randint(0, 5)

print('Result is...')

if userNumber == drawNumber:
    print('Congratulations you got the right number!')
else:
    print('You didn\'t get the right number! The number draw has {}.'.format(drawNumber))