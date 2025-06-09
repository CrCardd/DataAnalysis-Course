quantidade = int(input("Digite quantos alunos deseja cadastrar:\n>> "))
alunos = {}

for _ in range(quantidade):
    print("\n\n\n")
    new = {}
    nome = input("Insira o nome do aluno:\n>>")
    new["Idade"] = int(input(f"Insira a idade do(a) {nome}:\n>> "))
    new["Hobby"] = input(f"Insira o hobbie favorito do(a) {nome}:\n>> ")
    alunos[nome] = new


for aluno in alunos:
    print(100*"=")
    print(f"||\tNome:\t{aluno}")
    print(f"||\tIdade:\t{alunos[aluno]['Idade']}")
    print(f"||\tHobby:\t{alunos[aluno]['Hobby']}")
print(100*"=")