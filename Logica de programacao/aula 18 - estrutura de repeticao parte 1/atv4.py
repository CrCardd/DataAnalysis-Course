valores = []
quantidade = int(input("Digite quantos valores voce deseja inserir:\n>> "))
for i in range(quantidade):
    valores.append(int(input(f"Digite o valor [{i+1}]:  ")))
print(valores)