## mostre o dobro, o triplo e a raiz quadrada de um número
## raiz pode ser calculada com potencia elevada a 1/2
num = int(input('Type a number '))
raiz = pow(num, 1/2)
print('The double {}, the triple {}, and the square {:.3f}.'.format(num * 2, num * 3, raiz))