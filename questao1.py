preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto do produto: '))

valor = preco - (preco * desconto/100)

print('Valor final a pagar: ', valor)