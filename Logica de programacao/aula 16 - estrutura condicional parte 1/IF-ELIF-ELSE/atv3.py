operacoes = ["+", "-", "/", "*"]

print("---------------------------")
print("\tCALCULADORA\ta () b = ?")
print("---------------------------")
print(f"\t\t[1] - {operacoes[0]}")
print(f"\t\t[2] - {operacoes[1]}")
print(f"\t\t[3] - {operacoes[2]}")
print(f"\t\t[4] - {operacoes[3]}")
print("---------------------------")

operacao = int(input("Escolha uma operação:\n>> "))

if operacao > 3:
    print("operacao invalida!")
elif operacao < 0:
    print("operacao invalida!")

else:
    print("\n")
    a = int(input("a = "))
    b = int(input("b = "))

    print(f"{a} {operacoes[operacao]} {b} = ", end="")
    if operacao == 1:
        print(a + b) 
    if operacao == 2:
        print(a - b) 
    if operacao == 3:
        print(a / b) 
    if operacao == 4:
        print(a * b) 
