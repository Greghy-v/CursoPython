#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

print('Comprimento do cateto oposto: {:.2f}\nComprimento do cateto adjacente: {:.2f}'.format(co,ca))
print('Comprimento da hipotenusa: ',sqrt(co**2+ca**2))