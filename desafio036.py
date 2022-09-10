valcasa=float(input('Digite o valor do imóvel:'))
sal=float(input('Digite o seu salário:'))
anos=int(input('Digite em quantos anos você pagará:'))
prestmensal=valcasa/(anos*12)
print(f'A prestação mensal é {prestmensal:.2f}')
if prestmensal > sal*0.3:
    print('\033[4;31mVocê não poderá financiar esta casa, pois o valor excedeu 30% do seu salário\033[m')
else:
    print('Parabéns, \033[4;32mVocê poderá finaciar essa casa!!!\033[m')