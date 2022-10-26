# ler o primero termo e a razão da progressão aritmética e mostrar os 10 termos dessa progressão

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razao

for i in range(primeiroTermo, decimoTermo + razao, razao):
    print('{}'.format(i), end='-> ')

print('Fim da PA')