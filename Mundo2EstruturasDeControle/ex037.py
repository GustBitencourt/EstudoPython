# entrada número inteiro
# apresente as opções de converter para binário, octal e hexadecimal o número inteiro

num = int(input('Type a number '))
print('Escolha uma base para conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
option = int(input('Sua opção '))

if option == 1:
    print('{} num convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} num convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} num convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inexistente.')
