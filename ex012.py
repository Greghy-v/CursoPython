#faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto
p = float(input('Digite o preço do produto que deseja aplicar 5%' ' de desconto: '))
d = p-p*(5/100)
print('O preço final do produto é {:.2f}.'.format(d))
