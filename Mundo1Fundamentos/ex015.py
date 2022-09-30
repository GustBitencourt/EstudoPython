# quantidade de dias e kilometros rodados para retornar valor de alguel
# 60.00 por dia e 0.15 por km rodado
dias = int(input('Quantidade de dias alugados '))
km = int(input('Quantidade de Km rodados '))
aluguel = (dias * 60) + (km * 0.15)
print('O alguel ficou por {:.2f}'.format(aluguel))