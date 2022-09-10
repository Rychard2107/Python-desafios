from math import hypot
print('CALCULADOR DE HIPOTENUSA')
l1 = int(input('Digite o primeiro lado do triângulo:'))
l2 = int(input('Digite o segundo lado do triângulo:'))
hipo = hypot(l1, l2)
print(f'A hipotenusa do triângulo é {hipo:.2f}')

