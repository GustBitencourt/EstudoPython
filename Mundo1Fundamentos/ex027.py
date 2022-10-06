# pegue o primeiro e o útimo nome da entrada

name = str(input('Enter with your fullname ')).strip()
separaName = name.split()

print('Seu primeiro nome é {} e o seu último é {}'.format(separaName[0], separaName[len(separaName) -1]))