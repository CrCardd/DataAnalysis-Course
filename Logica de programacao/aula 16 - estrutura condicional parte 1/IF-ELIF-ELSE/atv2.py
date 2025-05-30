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
print(f"\nO computador jogou:\t{opcoes[computador]}\n\n")


if jogador - computador == 1:
    print("Voce venceu!!")
elif abs(jogador - computador) == len(opcoes)-1:
    print("Voce venceu!!")
elif jogador == computador :
    print("Empate...")
else: 
    print("Voce perdeu. :(")

