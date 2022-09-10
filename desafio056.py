idadehmvelho = int(0)
idadet = int(0)
contadorm = int(0)
for i in range(1,5):
    nome=str(input(f'Digite o \033[1;34mnome\033[m da {i}ª pessoa:'))
    idade=int(input(f'Digite a \033[1;34midade\033[m da {i}ª pessoa:'))
    sexo=str(input(f'Digite o \033[1;34msexo\033[m da {i}ª pessoa:'))
    if sexo == 'masculino' or sexo == 'm' and idade > idadehmvelho or idadehmvelho == 0:
        nomehmvelho = nome
        idadehmvelho = idade
    idadet = idadet + idade
    if sexo == 'feminino' or sexo == 'f' and idade < 20:
        contadorm += 1
idade = idadet / 4
print(f'A média das idades foi {idade}.')
print(f'A idade de {nomehmvelho} é {idadehmvelho} anos e ele é o homem mais velho.')
print(f'A quantidade de mulheres com menos de 20 anos foi {contadorm}.')