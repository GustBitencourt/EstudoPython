# programa que pergunte os Km da viagem do usuário e mostre o preço 0.50 por km para menores de 200km e 0.45 para maiores

tripKm = int(input('Enter how many Km your trip will be: '))

print('{} km'.format(tripKm))

if (tripKm <= 200):
    print('The price of your trip will be {:.2f}'.format(tripKm * 0.50))
else:
    print('The price of your trip will be {:.2f}'.format(tripKm * 0.45))