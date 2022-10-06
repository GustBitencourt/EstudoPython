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

## Módulos

- Utilizamos o import para importar módulos externos
- Instalamos bibliotecas externas com pip nomeBiblioteca
- Exemplos:

```python
import bebida
from bebida import
```

## Manipulando Textos

- Cada caractere possui indice
- len() trás o número de indices
- count pode contar o ocorrencia de um indice
  - pose ser usado com o fatiamento frase.count('o',0,13)
- find() indica onde encontra a ocorrencia indicada
  - se não encontrar indica -1
- replace() podemos alterar uma occorencia por outra frase.replace('Python', 'JavaScript')
- Fatiando frase[9:13] pega do caracter de indice 9 até o 12, já que o o 13 é excluído
- Inserindo intervalo de captura com frase[9:21:2] selecionára a cada dois indices partindo do primeiro
- Omitir o primeiro significa começar do inicio frase[:5]
- Omitir o final significa começar do indice indicado e ir até o último frase[4:]
- Podemos inserir intervalo com os exemplos acima [4::2]
- upper() deixa em maiúsculo
- lower() deixa em minúsculo
- capitalise() deixa apenas a primeira letra da frase em Maiúsuclo
- title() deixa todas as primeiras letras em maiúsuclos
- strip() remove os espaços inuteis
- rstrip() remove os espaços inuteis a direita
- lstrip() remove os espaços inuteis a esquerda
- split() separa a frase nos espaços
- '-'.join() junta a frase separada por indices,separando por traços
- print(""" """) vai imprimir o conteúdo com sua quebra de linha
- podemos combinar métodos
