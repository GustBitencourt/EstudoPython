# faça um programa que recebe o primeiro termo e a razão de uma PA, mostrando os 10 primeiros números
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

contador = 1
termo = primeiroTermo

while contador <= 10:    
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1

print('FIM.')