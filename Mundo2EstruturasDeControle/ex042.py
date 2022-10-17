reta1 = float(input('Type a number '))
reta2 = float(input('Type a number '))
reta3 = float(input('Type a number '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores, {}, {} e {} PODEM FORMAR um triangulo'.format(reta1, reta2, reta3), end=' ')

    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 and reta1 != reta3:
        print('ESCALENO')
    else:
        print('ISÓCELES')

else:
    print('Os valores, {}, {} e {} NÃO PODEM FORMAR um triangulo'.format(reta1, reta2, reta3))
