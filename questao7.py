x = int(input('Digite o seu CPF: '))
for y in str(x):
    if y != 11:
        print('CPF inválido.')
    else:
        print('CPF válido.')