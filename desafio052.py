primo = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for i in range(1, primo + 1):
    if primo % i == 0:
        cont += 1
if cont == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')