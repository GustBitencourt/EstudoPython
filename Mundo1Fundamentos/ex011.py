# programa que leia altura e largura de uma parede e calcule a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta 2m²

altura = float(input('Enter wall height '))
largura = float(input('Enter wall width '))
area = altura * largura

print('The wall has {:.2f}m² and can be painted with {:.2f} liter(s) of paint'.format(area, (area/2)))
