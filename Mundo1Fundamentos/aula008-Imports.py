from math import sqrt
import random

num = int(input('Type a number '))
num2 = random.randint(1, 10)
raiz = sqrt(num)
print('A raiz de {} é igual a {}. E o número sorteado foi {}'.format(num, raiz, num2))

