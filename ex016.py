#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
#porção inteira
from math import trunc
r = float(input('Digite o um número real qualquer e veja sua parte inteira: '))
print('O número real {} possui {} como parte inteira.'.format(r,trunc(r)))