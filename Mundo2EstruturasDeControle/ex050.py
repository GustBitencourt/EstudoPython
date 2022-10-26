# usuário insere 6 números somando apenas os pares

soma = 0
cont = 0
for i in range(1, 6 + 1):
    num = int(input('Type a number '))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Foram verificados {} números pares, sua soma é {}.'.format(cont, soma))