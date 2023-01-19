#escreva um programa que leia um valor em metros e exiba em centimetros e milimetros
m = float(input('Escreva o valor em metros: '))
cm = m*100
mm = m*1000
print('{} metros é equivalente a {} centímetros e {} milímetros.'.format(m,cm,mm))
