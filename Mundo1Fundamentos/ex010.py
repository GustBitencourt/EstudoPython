# coloque o valor em reais e mostre quantos dólares podem ser comprado, valor dólar 5,41
reais = float(input('Digite quantos reais tem dísponivel para compra de dólares '))
dolar = 5.41
cov = reais / dolar
print('Você pode adquirir {:.2f} dólares'.format(cov))