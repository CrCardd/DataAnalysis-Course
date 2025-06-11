a = int(input("Lado A:\n>> "))
b = int(input("Lado B:\n>> "))
c = int(input("Lado C:\n>> "))

perimetro = a+b+c
maior = max([a,b,c])
lados = [a,b,c]

lados_menor = lados[:]
lados_menor.remove(maior)
if maior in lados_menor:
    lados_menor.remove(maior)

if perimetro/3 == a and perimetro/3 == b and perimetro/3 == c:
    print("equilatero")
elif len(lados_menor) == 1 or lados_menor[0] == lados_menor[1]:
    print("isoceles")
elif maior ** 2 == lados[0] ** 2 + lados[1] ** 2:
    print("retângulo")