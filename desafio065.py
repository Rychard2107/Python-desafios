i = 'S'
d=int(0)
acnum=int(0)
maior=int(0)
menor=int(1000)

while i in 'S':
    num=int(input('Digite um número:'))
    i=str(input('Você quer continuar?[S/N]')).strip().upper()[0]
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    acnum = acnum + num
    d += 1
media = acnum/d
print(f'O maior número foi {maior} e o menor número foi {menor}')
print(f'A média dos números foi {media:.1f}')