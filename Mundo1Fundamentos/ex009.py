# entrada de um número e mostre sua tabuada
num = int(input('Type a number '))
for number in range(0, 11):
    print('{} X {} = {} '.format(num, number, num * number))


