# programa que leia nome, idade e sexo de 5 pessoas
# retorna a média de idade
# homem mais velho
# quantas mulheres menores de idade

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemVelho = ''
totalMulheresMenores = 0
for pessoa in range(1, 6):
    print('---{}ª Pessoa---'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F')).strip()
    somaIdade += idade

    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    elif sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    
    
    if sexo in 'Ff' and idade < 18:
        totalMulheresMenores += 1

    


mediaIdade = somaIdade / 5
print('Média de idade de {} anos'.format(mediaIdade))
print('O {} é o homem mais velho e tem {} anos'.format(nomeHomemVelho, maiorIdadeHomem))
print('A {} mulheres menores de idade'.format(totalMulheresMenores))
