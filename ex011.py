#faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la
#1 litro de tinta = 2m²
a = float(input('Digite a altura de sua parede em metros: '))
l = float(input('Digite a largura de sua parede em metros: '))
area = a*l
t = area/2
print('Para pintar a sua parede serão necessários',t,'balde(s) de tinta.')
