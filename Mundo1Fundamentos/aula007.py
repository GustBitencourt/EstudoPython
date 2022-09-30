num1 = float(input('Type a number '))
num2 = float(input('Type a number '))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2
divIn = num1 // num2
rest = num1 % num2

print('The results above are for the sum {}, sub {}, and mult {}, div {:.4f}, and divIn {}, exp {} and the rest {}'.format(sum, sub, mult, div, divIn, exp, rest))