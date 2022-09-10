from random import choice
maqesc=choice(['pedra','papel','tesoura'])
escolha=str(input('\033[1;30;107mBEM VINDO AO JOKENPÔ CONTRA A MÁQUINA\033[m\n'
                  'Escolha pedra, papel ou tesoura:'))
if maqesc == escolha:
    print(f'A máquina escolheu {maqesc} e você escolheu {escolha}, portanto foi \033[1;33mempate\033[m.')
elif maqesc == 'pedra' and escolha == 'tesoura' or maqesc == 'papel' and escolha == 'pedra' or maqesc == 'tesoura' and escolha == 'papel':
    print(f'A máquina escolheu {maqesc} e você escolheu {escolha},portanto \033[1;31mVOCÊ PERDEU PARA A MÁQUINA!!!\033[m')
elif escolha == 'pedra' and maqesc == 'tesoura' or escolha == 'papel' and maqesc == 'pedra' or escolha == 'tesoura' and maqesc == 'papel':
    print(f'A máquina escolheu {maqesc} e você escolheu {escolha}, portanto \033[1;32mVOCÊ VENCEU A MÁQUINA!!!\033[m')
else:
    print('Verifique se você digitou corretamente(tudo em minúsculo)')