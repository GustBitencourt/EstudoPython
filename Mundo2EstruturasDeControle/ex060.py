#recebe um número e mostre seu fatorial

num = int(input('Type a number '))
total = 1


while num > 0:
    print('{}'.format(num), end='')
    print(' X ' if num > 1 else ' = ', end='')
    total *= num
    num -= 1

print('{}'.format(total))
print('FIM')

