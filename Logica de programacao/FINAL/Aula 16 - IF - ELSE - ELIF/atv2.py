import random as rd

opcoes = ["tesoura", "pedra", "papel"]

print("---------------------------")
print(f"\t1 - {opcoes[0]}")
print(f"\t2 - {opcoes[1]}")
print(f"\t3 - {opcoes[2]}")
print("---------------------------")
jogador = int(input("Escolha sua jogada:\n>> "))
jogador -= 1

computador = rd.randint(0,len(opcoes)-1)
try:
    print(f"\nVocê jogou:\t\t{opcoes[jogador]}")
    print(f"Computador jogou:\t{opcoes[computador]}\n")

    if jogador - computador == 1:
        print("Voce venceu!!")
    elif -(jogador - computador) == len(opcoes)-1:
        print("Voce venceu!!")
    elif jogador == computador :
        print("Empate...")
    else: 
        print("Voce perdeu. :(")

except:
    print("Escolha um indice valido...")

