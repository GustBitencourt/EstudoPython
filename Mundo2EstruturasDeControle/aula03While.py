print('============Exemplo1===============')
# com for
for i in range(1, 10):
    print(i)

print('Fim For!')


i = 1
while i < 10:
    print(i)
    i += 1
print('End While1')

print('\n============Exemplo2===============')
# while como comando para parar ao digitar 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('End While2')


print('\n============Exemplo3===============')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('End While3')


print('\n============Exemplo4===============')
num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))

    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1            
print('Você digitou {} números PARES e {} números ímpares'.format(par, impar))
print('End While4')

