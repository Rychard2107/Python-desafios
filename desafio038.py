num = int(input('Bem vindo ao \033[1;34mConversor de Números\033[m, digite o número que você quer converter:'))
print('Se você deseja transformar em Binario tecle 1\n'
      'Se você deseja transformar em octal tecle 2\n'
      'Se você deseja transformar em hexadecimal tecle 3')
escolha = int(input('Em qual categoria você deseja transformar?'))
if escolha == 1:
    binario = bin(num)
    print(f'O numero em binario foi de {binario}.')
elif escolha == 2:
    octal = oct(num)
    print(f'O numero em Octal foi de {octal}.')
elif escolha == 3:
    hex = hex(num)
    print(f'O numero em Hexadecimal foi de {hex}.')
else:
    print('Escolha apenas numeros de 1 a 3!')