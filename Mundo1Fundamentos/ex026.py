# verifica quantas vezes aparece a letra a na frase e onde é sua primeira e última ocorrencia

sentence = str(input('Type a sentence ')).strip().upper()

print('A aparece {} vezes'.format(sentence.count('A')))
print('A primeira ocorrencia de A é na posição {}'.format(sentence.find('A') + 1))
print('A última ocorrencia de A é na posição {}'.format(sentence.rfind('A') + 1))