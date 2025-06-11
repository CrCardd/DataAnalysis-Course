import random as rd

secret = rd.randint(0,10)

while True:
    a = int(input('Tente adivinhar o número entre 0 e 11:\n>> '))
    if a == secret:
        break

print('\nAcertou!')