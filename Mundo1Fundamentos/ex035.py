# verifique se três retas podem formar um triângulo
reta1 = float(input('Type a number '))
reta2 = float(input('Type a number '))
reta3 = float(input('Type a number '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores, {}, {} e {} PODEM FORMAR um triangulo'.format(reta1, reta2, reta3))
else:
    print('Os valores, {}, {} e {} NÃO PODEM FORMAR um triangulo'.format(reta1, reta2, reta3))
