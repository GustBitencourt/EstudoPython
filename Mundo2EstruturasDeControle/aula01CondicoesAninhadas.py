nome = str(input('Type your name ')).strip().upper()

if nome == 'GUSTAVO':
    print('Olá ser de beleza única!')
elif nome == 'MARIA' or nome == 'JOÃO' or nome == 'JOSÉ':
    print('Olá belo(a) mortal')
elif nome in 'Ana Patricia Priscilla Julia':
    print('Olá exemplar feminino')
else:
    print('Olá ser de beleza inferior')

print('Tenha um bom dia {}'.format(nome))