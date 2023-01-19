#crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#1dol = 3,27brl
c = float(input('Digite quanto dinheiro você possui na sua carteira: '))
dol = c/3.27
print('Atualmente você possuí {}, com esse valor você conseguirá comprar {:.2f} dólares.'.format(c,dol))
