for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa:'))
    if i == 1:
        maiorp = peso
        menorp = peso
    if maiorp < peso:
        maiorp = peso
    if menorp > peso:
        menorp = peso
print(f'o maior peso foi {maiorp} e o menor peso foi {menorp}')