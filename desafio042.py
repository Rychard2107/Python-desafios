r1=int(input('Digite o primeiro lado do triângulo:'))
r2=int(input('Digite o segundo lado do triângulo:'))
r3=int(input('Digite o terceiro lado do triângulo:'))
if abs(r2-r3)<r1<r2+r3 and abs(r1-r3)<r2<r1+r3 and abs(r1-r2)<r3<r1+r2:
    print('Pode formar um triângulo')
    if r1 != r2 != r3:
        print('É um triângulo escaleno')
    elif r1 == r2 == r3:
        print('É um triângulo equilátero')
    else:
        print('É um triângulo isósceles')
else:
    print('Não pode formar um triângulo')