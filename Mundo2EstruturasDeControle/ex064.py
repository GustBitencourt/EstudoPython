# recebe números e soma eles enquanto o usuário quiser

num = int(input('Type a number: '))
total = 0
contador = 0

while num != 999:
    total += num
    contador += 1
    num = int(input('Type a number, if you want to stop type [999]: '))

print('Foram somados {} números o resultado foi de {}'.format(contador, total))