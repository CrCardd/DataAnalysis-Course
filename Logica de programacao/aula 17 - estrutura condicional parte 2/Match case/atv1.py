def main():
    operacoes = ["+", "-", "/", "*", "^"]

    print(40*"-")
    print("\tCALCULADORA\ta () b = ?")
    print(40*"-")
    print(f"\t\t[1] - {operacoes[0]}")
    print(f"\t\t[2] - {operacoes[1]}")
    print(f"\t\t[3] - {operacoes[2]}")
    print(f"\t\t[4] - {operacoes[3]}")
    print(f"\t\t[5] - {operacoes[4]}")
    print(40*"-")

    operacao = int(input("Escolha uma operação:\n>> "))
    if(operacao < 1 or operacao > len(operacoes)):
        print("Escolha uma operação válida.....")
        return

    a = int(input("a = "))
    b = int(input("b = "))

    print(f"{a} {operacoes[operacao-1]} {b} = ", end="")

    match operacao:
        case 1:
            print(a + b) 
        case 2:
            print(a - b) 
        case 3:
            print(a / b) 
        case 4:
            print(a * b) 
        case 5:
            print(a ** b) 
        

main()