
print('\033[1;34mCALCULO DE FATORIAL\033[m')
n=int(input('Digite um número para descobrir o seu fatorial:'))
fat = 1
i = 2
while i <= n:
        fat = fat*i
        i = i + 1
print('O fatorial de {} é {}: '.format(n, fat))
