contador = 0
frase = input('Digite uma frase: ')
for x in list(frase):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        contador += 1

print(f' A quantidade total de vogais é: {contador}')