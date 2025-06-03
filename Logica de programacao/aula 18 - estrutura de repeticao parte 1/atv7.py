numero = int(input("Digite um número para ser verificado: "))

numero = 11
primo = True
for n in range(2, int(numero ** 0.5)+1):
    if numero % n == 0:
            primo = False
            break

print(primo)