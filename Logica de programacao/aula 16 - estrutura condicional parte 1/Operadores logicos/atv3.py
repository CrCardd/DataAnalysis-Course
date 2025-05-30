import random as rd

numero_secreto = rd.randint(0,100)

print("Tente adivinhar o número secreto entre -1 e 101")
a = int(input("Inicio da análise:\n>> "))
b = int(input("Fim da análise:\n>> "))

if(a > b):
    print("o inicio da análie não deve ser maior do que o fim")
else:
    if(a < numero_secreto and numero_secreto < b):
        print("O número secreto está entre o intervalo fornecido")
    elif(a > numero_secreto):
        print("O número secreto está para trás do intervalo de análise")
    elif(b < numero_secreto):
        print("O número secreto excedeu o intervalo de análise")
    else:
        print("O número secreto é um dos delimitadores.....")

    chute = int(input("Adivinhe o numero secreto:\n>> "))

    print("------------------")
    print(f"|     - {numero_secreto} -     |")
    print("------------------")
    if(chute == numero_secreto):
        print("\n\nVoce acertou!!")
    else:
        print("\n\nNão sobrou nada...")
