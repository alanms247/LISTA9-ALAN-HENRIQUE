import random
x = random.randint(1,100)
for z in range(1, 999):
    y = int(input('Tente acertar o número de um à cem: '))
    if y != x:
        if (x - y) < 0:
            y = (y * -1)
        if (x - y) < 10:
            print('Está próximo!')
        elif (x - y) < 30:
            print('Está frio!')
        else:
            print('Está muito frio!')
    else:
        print(f'Acertou! O número era {x}')