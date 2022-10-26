# verifique se uma frase é um palindromo desconsiderando espaços e assentos

frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
agrupandoPalavras = ''.join(palavras)
fraseContraria = ''

print('Frase digitada: {}'.format(frase))

for letra in range(len(agrupandoPalavras) -1, -1, -1):
    fraseContraria += agrupandoPalavras[letra]

if fraseContraria == agrupandoPalavras:
    print('A frase {} é um PALÍNDROMO: {}.'.format(frase, fraseContraria))
else:
    print('A frase {} NÃO é um PALÍNDROMO: {}.'.format(frase, fraseContraria))


print('\n==============Exemplo2==================')
inversando = agrupandoPalavras[::-1]
print(agrupandoPalavras)