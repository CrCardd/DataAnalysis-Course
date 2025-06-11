import random as rd

secret = rd.randint(0,10)

while a != secret:
    a = int(input('Tente adivinhar o número entre 0 e 11:\n>> '))

print('\nAcertou!')