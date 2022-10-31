# programa que só aceite entrada mf qualquer coisa diferente ele requisita a resposta novamente

res = str(input('Digite seu sexo. [M/F] ')).strip().upper()

while res != 'M' and res != 'F':
    res = str(input('Digite novamente M ou F ')).upper()

print('Sua resposta {} foi enviada.'.format(res))


print('\n==========Exemplo Guanabara==========')
res2 = str(input('Digite seu sexo. [M/F] ')).strip().upper()[0]

while res2 not in 'MmFf':
    res2 = str(input('Digite novamente M ou F ')).upper()[0]

print('Sua resposta {} foi enviada.'.format(res2))