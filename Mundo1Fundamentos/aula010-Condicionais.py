tempo = int(input('Digite quantos anos tem o seu carro '))

if tempo <= 3:
    print('carro novo amor')
else:
    print('lata velha')



name = input('Type your name ')

if name == 'Gustavo':
    print('Hello BOSS')
print('Bom dia {}'.format(name))


n1 = float(input('Digite a nota1 '))
n2 = float(input('Digite a nota2 '))
media = (n1 + n2) / 2

if media < 6:
    print('Média de {}. Está de recuperação'.format(media))
else:
    print('Média de {}. Não é necessário recuperação'.format(media))