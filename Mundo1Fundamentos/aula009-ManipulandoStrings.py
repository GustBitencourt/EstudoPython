frase = 'Curso em vídeo Python'
fraseSplit = frase.split()

print('lenght', len(frase))
print('count', frase.count('o'))
print('count', frase.count('o',0,13))
print('find', frase.find('video'))

print(frase[10])
print(frase[9:13])
print(frase[9:21])
print(frase[4:21:2])
print(frase[:10])
print(frase[10:])
print(frase[9::3])

print('replace', frase.replace('Python', 'JavaScript'))
print('split', fraseSplit)
print('join', '-'.join(fraseSplit))