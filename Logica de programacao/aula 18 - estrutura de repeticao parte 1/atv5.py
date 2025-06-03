base = int(input("Tamanho da pirâmide:\n>> "))

for i in range(base):
    print((base-i)*" ", end="")
    print(i*"X ")