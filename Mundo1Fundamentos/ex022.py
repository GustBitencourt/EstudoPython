# nome em maiusculo, minusculo, conte as letras do nome completo sem espaço, 
# separe o primeiro nome e conte as letras

name = input('Type your fullname ').strip()
print('Nome em maiúsculo, {}'.format(name.upper()))
print('Nome em minúsculo, {}'.format(name.lower()))
print('Seu nome possui {} letras'.format(len(name) - name.count(' ')))
firstName = name.split()[0]
print('Seu primeiro nome é {} e possui {} letras'.format(firstName, len(firstName)))
print('Seu primeiro nome possui {} letras'.format(name.find(' ')))
