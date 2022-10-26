# mostre a tabuado do número que o usuário escolher

num = int(input('Type a number '))
for i in range(1, 10 + 1):
    print('{} X {} = {}'.format(num, i, i * num))