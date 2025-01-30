x = int(input('Digite o seu CPF: '))
cpf = str(x)
if len(cpf) != 11:
    print('CPF inválido.')
else:
    print('CPF válido.')