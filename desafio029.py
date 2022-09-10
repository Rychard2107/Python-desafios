velo = int(input('Digite a velocidade do seu carro:'))
if velo > 80:
    multa = (velo-80)*7
    print(f'você foi multado por escesso de velocidade em {multa:.2f}')
else:
    print('Você é um cidadão de bem')
