# programa que apresente opções de forma de pagamento
# recebe preço do produto, e forma de pagamento
# a vista com dinheiro 10% de desconto, com cartão 5%, 
# em até 2x preço normal, 3x ou mais 20% de juros

produto = float(input('Valor produto R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO
[ 2 ] À VISTA CARTÂO
[ 3 ] 2x NO CARTÂO
[ 4 ] 3x OU MAIS NO CARTÂO
''')

opcao = int(input('Escolha forma de pagamento: '))

if opcao == 1:
    total = produto * 0.9
    print('Preço do produto R$ {:.2f}, preço final após desconto R$ {:.2f}.'.format(produto, total))
elif opcao == 2:
    total = produto * 0.95
    print('Preço do produto R$ {:.2f}, preço final após desconto R$ {:.2f}.'.format(produto, total))
elif opcao == 3:
    total = produto * 1.05
    parcela = total / 2
    print('Preço do produto R$ {:.2f}, preço final após cobrança de taxas R$ {:.2f}. Com parcelas de R$ {:.2f}.'.format(produto, total, parcela))
elif opcao == 4:
    total = produto * 1.20
    quantidadeParcela = int(input('Quantas vezes deseja parcelar? '))
    parcela = total / quantidadeParcela
    print('Preço do produto R$ {:.2f}, preço final após cobrança de taxas R$ {:.2f}. Pagamneto em {} vezes com parcelas de R$ {:.2f} '.format(produto, total, quantidadeParcela, parcela))
else:
    print('Opção inexistente.')
