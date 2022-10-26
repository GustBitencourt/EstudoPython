# programa que mostre se um número é primo

num = int(input('Type a number '))
numsDivisiveis = []
qtdDividida = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        numsDivisiveis.append(i)
        qtdDividida += 1
    else:
        print('\033[31m', end='')
    print('{} - '.format(i), end='')
    
if qtdDividida == 2:
    print('\n\033[mO número {} é primo, foi divido por {}'.format(num, numsDivisiveis))
else:
    print('\nO número {} não é primo, e foi divido por {}'.format(num, numsDivisiveis))
    
