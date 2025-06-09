idade = int(input("Digite a sua idade:\n>> "))

if idade < 16:
    print("Seu voto não permitido")
elif idade > 17:
    print("Seu voto é obrigatório")
else:
    print("Seu voto é facultativo")
