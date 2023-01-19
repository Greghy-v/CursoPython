#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
perc = float(input('Digite a quantidade de quilômetros percorridos pelo seu carro: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
final = (perc * 0.15) + (dias * 60)
print('O valor total é de R${:.2f}.'.format(final))
