fibonacci = [0,1]

vezes = int(input("Digite quantos valores de fibonacci você deseja:\n>> "))
for i in range(vezes-2):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)