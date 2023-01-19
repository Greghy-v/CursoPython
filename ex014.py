#Faça um programa que converta a temperatura digitada em °C e converta para F°.
c = float(input('Digite a quantidade de °C: '))
f = c*1.8+32
print('{}°C é/são equivalente(s) a {:.2f}°F.'.format(c,f))
