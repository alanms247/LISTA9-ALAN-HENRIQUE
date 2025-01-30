nomes = []
z = 0
c = 0
for x in range(5):
    z += 1
    n = input(f'Digite seu nome: ({z}/5)\n')
    if n[0] == 'a':
        nomes.append(n)
        c += 1
print(f'Quantidade de nomes que começam com "a": {c}')
if nomes != []:
    print(nomes)