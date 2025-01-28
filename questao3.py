n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
p1 = int(input('Digite o peso da primeira nota: '))
p2 = int(input('Digite o peso da segunda nota: '))

media = ((n1*p1) + (n2*p2)) / (p1+p2)
print(f'A média ponderada das notas é: {media}')