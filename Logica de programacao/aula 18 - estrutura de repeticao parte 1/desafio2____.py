import math as mt
import random as rd

def printPiramide(piramide):
    prints = 0
    for m in range(1,base+1):
        print((base-m)*"    ", end = "")
        for n in range(m):
            print(f"{piramide[prints]}       ", end = "")
            prints += 1
        print("")
    print(100*"-")


def search(pivot, data, caminhos, base):
    delta = mt.sqrt( 8 * pivot + 2)
    camada = int((delta - 1) / 2) + int(delta > int(delta))
    
    if camada == base:
        return 0

    esquerda = search(pivot + camada, data, caminhos, base)
    direita = search(pivot + camada + 1, data, caminhos, base)
    caminhos[pivot] = int(direita > esquerda)

    return data[pivot] + esquerda if esquerda > direita else data[pivot] + direita


base = int(input("Base da pirâmide:\n>> "))
length = int((base * (base + 1)) / 2)


piramide = [rd.randint(0,100) for _ in range(length)]
caminhos = [0 for _ in range(length)]




melhorPontuacao = search(0, piramide, caminhos, base)

printPiramide(piramide)
printPiramide(caminhos)

print(f"\nMelhor pontuação:\t{melhorPontuacao}")

