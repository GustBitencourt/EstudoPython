from math import radians, cos, sin, tan
# digite um angulo e mostre seu seno, cosseno, e tangente
# necessário converter para radiano primeiramente

ang = float(input('Type a angle '))
print('O angulo {} tem como cosseno {:.2f}, seno {:.2f} e tangente {:.2f}'.format(ang, cos(radians(ang)), sin(radians(ang)), tan(radians(ang))))