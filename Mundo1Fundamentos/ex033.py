# programa que leia tres numeros e verifique qual é o maior
from random import randint

num1 = randint(0, 500)
num2 = randint(0, 500)
num3 = randint(0, 500)

print('The numbers drawed are num1 {}, num2 {}, num3 {}'.format(num1, num2, num3))

#verificando menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#verificando maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O MAIOR número sorteado foi {}'.format(maior))
print('O MENOR número sorteado foi {}'.format(menor))