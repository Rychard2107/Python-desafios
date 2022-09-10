
print('Preço da viagem até 200km é \033[4;34mR$0,50\033[m por km\n'
      'Depois de 200km passa a ser \033[4;34mR$0,45\033[m')
D = float(input('digite a distância da viagem:'))
if D<=200:
    valor = D * 0.5
    print(f'O valor da passagem é \033[4;34mR${valor:.2f}\033[m!!!')
else:
    valor = D * 0.45
    print(f'O valor da passagem é \033[4;34mR${valor:.2f}\033[m!!!')