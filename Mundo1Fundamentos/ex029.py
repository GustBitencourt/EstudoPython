# programa que leia a velocidade do carro, se for acima do limite cobre 7 reais por kilometro acima
from random import randint

speedLimit = 80
carSpeed = randint(70, 120)
fine = (carSpeed - speedLimit) * 7

print('Your speed is {} Km.'.format(carSpeed))
if(carSpeed <= speedLimit):
    print('You are at a safe speed')
else:
    print('You were fined, your fine is R$ {:.2f}'.format(fine))
