# demonstre as casas numéricas da entrada do usuário
num = int(input('Enter with a number between 0 and 9999 '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Analyzing {}'.format(num))
print('O número na casa da milhar é {}'.format(milhar))
print('O número na casa de centena é {}'.format(centena))
print('O número na casa de dezena é {}'.format(dezena))
print('O número na casa da unidade é {}'.format(unidade))