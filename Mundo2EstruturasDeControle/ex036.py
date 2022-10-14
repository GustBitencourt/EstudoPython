# programa que apure o empréstimo bancário para a compra de uma casa
# entradas valor da casa, salário comprador, e em quantos anos ele quer realizar o pagamento
# a prestação não pode ser maior que 30% do valor do sálario

precoCasa = float(input('Valor da casa '))
salario = float(input('Salário do comprador '))
anosPagando = int(input('Em quantos anos deseja realizar o pagamento '))

parcelaMes = precoCasa / (anosPagando * 12)
salario30 = salario * 0.30


if parcelaMes <= salario30:
    print('O pagamento do imóvel com valor de R${:.2f} em {} anos será com uma parcela de R${:.2f}.'.format(precoCasa, anosPagando, parcelaMes))
else:
    print('Empréstimo NEGADO, a parcela excede em 30% os seus rendimentos.')