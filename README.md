# Python Curso em vídeo

## Tipos Primitivos

- Strings
- Numbers, ints or floats
- Booleans

## Exemplo Formatação

```python
num1 = int(input('Type a number '))
num2 = int(input('Type a number '))
soma = num1 + num2
print('The sum between {} and {} is {}'.format(num1, num2, soma))
```

- Formatação dentro de um espaço:
    1. alinha a direita  >
    2. alinha a esquerda <
    3. centraliza        ^
    4. colocando algum sinal antes do sinal de alinhamento ele preenche o espaço vazio com esse sinal

- Formatação com sinais
    1. usando :.3f dentro de uma máscara, que recebe um número, escolhemos a quantidade de números após a virgula
    2. utilazando \n na construção da string você quebra linha
    3. end = ' ' você agrupa os prints separados por um espaço
  
```python
name = input('type your name')
print('Welcome to the jungle {}!'.format(:>20))
```

## Operadores Aritméticos

- Adição            +
- Subtração         -
- Multiplicação     *
- Potência          **
- Divisão           /
- Divisão inteira   //
- Resto da divisão  %
  