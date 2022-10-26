# ler o peso de 5 pessoas mostrar o maior e o menor peso
maior = 0

for pessoa in range(1, 6):
    peso = int(input('Peso pessoa {}: '.format(pessoa)))
    
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif menor > peso:
            menor = peso

print('MAIOR peso {}kg'.format(maior))
print('MENOR peso {}kg'.format(menor))