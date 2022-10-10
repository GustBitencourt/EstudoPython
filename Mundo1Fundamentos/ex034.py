# programa que de aumento de 10% para salários maiores ou iguais a 1250.00 e de 15% para menores que isso
from random import randint
salary = randint(1200, 1300)

print('Employee salary: {:.2f}'.format(salary))
if(salary > 1250):
    print('You got a 10% raise. Now your salary is {:.2f}'.format(salary * 1.10))
else:
    print('You got a 15% raise. Now your salary is {:.2f}'.format(salary * 1.15))