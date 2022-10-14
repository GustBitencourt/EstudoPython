# Compare números e retorne o maior

num1 = int(input('Type a number '))
num2 = int(input('Type a number '))

if num1 > num2:
    print('O primeiro valor {} é maior que o segundo {}'.format(num1, num2))
elif num2 < num1:
    print('O segundo valor {} é maior que o primeiro {}'.format(num2, num1))
else:
    print('Os valores são iguais')