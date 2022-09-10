num=int(input('Digite um número:'))
print('\033[1;97;40mTABUADA\033[m')
for i in range(1,11):
    r = num*i
    print(f'{num} x {i} = {r}')
