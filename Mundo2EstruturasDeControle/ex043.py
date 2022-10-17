# programa que calcule o IMC
# entrada altura e peso
# 18.5 abaixo do peso, ate 25 peso ideal, até 30 sobrepeso, até 40 obesidade, acima de 40 obesidade mórbidade

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura ** 2)

print ('IMC igual a {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está na faixa de peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')