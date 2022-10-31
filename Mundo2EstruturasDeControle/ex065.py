# programa que leia vários números inteiros, ao final mostre a média de valores, o maior númeor e o menor número, e pergunte se o usuário quer ou não continuar a inserir valores

resposta = 'S'
total = 0
contador = 0

while resposta in 'Ss':
    num = int(input('Type a number: '))
    
    total += num
    contador += 1

    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = total / contador
print('Númemros digitados {}, O MAIOR número é {}, o MENOR {}, a MÉDIA {}'.format(contador, maior, menor, media))


