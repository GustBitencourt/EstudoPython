# programa que leia um numero inteiro e mostre se ele é par ou impar
from random import randint

num = randint(1, 1000)

print('Num is {}'.format(num))
if (num % 2 == 0):
    print("Even")
else:
    print("Odd")