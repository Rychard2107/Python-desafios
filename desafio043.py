peso=float(input('Digite seu peso(kg):'))
altura=float(input('Digite sua Altura(m):'))
imc=peso/altura**2
print(f'Seu IMC é \033[1;34m{imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Pré-obesidade')
elif imc <= 34.9:
    print('Obesidade Grau 1')
elif imc <= 39.9:
    print('Obesidade Grau 2')
else:
    print('Obesidade Grau3')
