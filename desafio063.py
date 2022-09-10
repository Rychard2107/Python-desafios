n = int(input('\033[1;34mQUANTOS TERMOS DA SEQUÊNCIA DE FIBONACCI VOCÊ QUER:\033[m'))
t3 = int(0)
t1 = int(0)
t2 = int(1)
print(f'{t1}')
print(f'{t2}')
for i in range(1, n-1):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)

