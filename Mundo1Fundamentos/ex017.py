from math import hypot 
# calcule a hipotenusa através do cateto oposto e adjacente

catOp = float(input('Cateto oposto '))
catAd = float(input('Cateto adjacente '))

hipoSemMod = (catOp ** 2 + catAd ** 2) ** (1/2)
hipoMod = hypot(catOp, catAd)

print('Com o cateto oposto de {} e o cateto adjacente de {} o valor da hipotenusa é {}'.format(catOp, catAd, hipoSemMod))
print('Com o cateto oposto de {} e o cateto adjacente de {} o valor da hipotenusa é {}'.format(catOp, catAd, hipoMod))