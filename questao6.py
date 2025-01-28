p = 0
i = 0
for x in range(1, 11):
    y = int(input('Digite um número inteiro (10 no total): '))
    if y % 2 == 0:
        p += 1
    else:
        i += 1
print(f'Números pares no total: {p}\nNúmeros ímpares no total: {i}')
