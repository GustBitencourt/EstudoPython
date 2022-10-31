# faça um programa que recebe o primeiro termo e a razão de uma PA, mostrando os 10 primeiros números e que tenha a capacidade de mostrar caso o usuário queira
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

contador = 1
termo = primeiroTermo

total = 0
continuar = 10

while continuar != 0:
    total += continuar
    while contador <= total:    
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1

    print('FIM da análise inicial.')
    continuar = int(input('Gostaria de visualizar mais quantos termos? : '))
print('Amostra finalizada. Foi mostrado um total de {} termos'.format(total))