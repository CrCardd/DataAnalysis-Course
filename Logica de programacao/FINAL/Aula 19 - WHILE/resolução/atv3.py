import random as rd

secret = rd.randint(1,100)
a = 0
count = 0
while secret != a:
    a = int(input('\nTente adivinhar o número secreto:\n>> '))
    if a > secret:
        print(f'Abaixo')
    if a < secret:
        print(f'Acima')
    count += 1

print('\n\n')
print('+-----------------------+')
print('|       Acertou!!       |')
print('+-----------------------+')
print(f'| Número secreto: {secret}\t|')
print(f'| Palpites: {count}\t\t|')
print('+-----------------------+')