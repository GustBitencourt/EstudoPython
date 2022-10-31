# programa que recebe dois núemros como entrada e a operação escolhida pelo usuário


operation = (int(input('Escolha a operação que deseja realizar:\n[1] - SOMA \n[2] - SUBTRAÇÃO\n[3] - DIVISÃO\n[4] - MULTIPLICAÇÃO \n[5] - SAIR ')))

while operation != 5:

    num1 = int(input('Type a number '))
    num2 = int(input('Type a number '))

    if operation == 1:
        print('Resultado de {} + {} = {}'.format(num1, num2, (num1 + num2)))
    elif operation == 2:
        print('Resultado de {} - {} = {}'.format(num1, num2, (num1 - num2)))
    elif operation == 3:
        print('Resultado de {} / {} = {}'.format(num1, num2, (num1 / num2)))
    elif operation == 4:
        print('Resultado de {} * {} = {}'.format(num1, num2, (num1 * num2)))

    operation = (int(input('Escolha a operação que deseja realizar:\n[1] - SOMA \n[2] - SUBTRAÇÃO\n[3] - DIVISÃO\n[4] - MULTIPLICAÇÃO \n[5] - SAIR ')))

print('Sáida confirmada.')