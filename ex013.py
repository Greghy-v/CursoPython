#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
s = float(input('Digite o seu salário e veja quanto será com 15''%'' de aumento: '))
a = s+s*(15/100)
print('Seu salário passará de {} para {:.2f}.'.format(s,a))
