def get_data(path, split):
    with open(path, 'r') as file:
        cabecalho = file.readline().split(split)
        cabecalho[0] = 'Breed'
        dados = []
        for linha in file.readlines():
            linha = linha.split(split)
            dados_linha = {}
            for i in range(len(linha)):
                linha[i] = linha[i].strip()
                dados_linha[cabecalho[i].strip()] = linha[i]
            dados.append(dados_linha)
    return dados