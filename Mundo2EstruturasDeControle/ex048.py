# soma dos números múltiplos de tres ÍMPARES no intervalo entre 1 e 500

soma = 0
cont = 0
for i in range(1, 500 + 1):
    if not i % 2 == 0:
        if i % 3 == 0:
            soma += i
            cont += 1
    
print('A soma de todos os {} números verificados é igual a {} '.format(cont, soma))
