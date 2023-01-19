#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
d = int(n*2)
t = int(n*3)
rq = pow(n, (1/2))
print('O dobro de {} é {}, o triplo é {} e a raíz quadrada é {:.2f}'.format(n,d,t,rq))
