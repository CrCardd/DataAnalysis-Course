from lib import get_data

def filter(dados, colunas_comparacao):

    dados_retorno = []

    for linha in dados:
        valido_and = True
        for coluna in colunas_comparacao:
            valido_or = False
            for comparacao in colunas_comparacao[coluna]:
                if linha[coluna] == comparacao:
                    valido_or = True
            if not valido_or:
                valido_and = False 
        if valido_and:
            dados_retorno.append(linha)

    return dados_retorno
            

def map(dados, colunas_modificacao):
    dados_retorno = []
    for linha in dados:
        for coluna in colunas_modificacao:
            linha[coluna] = colunas_modificacao[coluna]
        dados_retorno.append(linha)

    return dados_retorno


def group(dados, colunas_reduzidas):
    dados_retorno = []
    
    for linha in dados:
        contem = False
        for linha_retorno in dados_retorno:
            contem = True
            for coluna in colunas_reduzidas:
                if not linha[coluna] in linha_retorno.values():
                    contem = False
        if not contem:
            linha_retorno = {i : [] if i not in colunas_reduzidas else linha[i] for i in dados[0]}
            dados_retorno.append(linha_retorno)



    for linha in dados:
        contem = False
        for i_dr in range(len(dados_retorno)):
            contem = True
            for coluna in colunas_reduzidas:
                if not linha[coluna] in dados_retorno[i_dr].values():
                    contem = False
                    

            if contem:
                for coluna in dados[0]:
                    if coluna in colunas_reduzidas:
                        continue
                    dados_retorno[i_dr][coluna].append(linha[coluna])

    return dados_retorno



dados = get_data('./gatos.csv', ';')

# filter() recebe os dados e um dicionário
# cada índice do dicionário corresponde a uma coluna
# o valor dos índices é uma lista, onde a coluna pode conter qualquer um dos valores que estão na lista
filtrados = filter(dados, {'Breed' : ['Maine coon', 'Angora']})

# map() recebe os dados e um dicionário
# cada índice do dicionário corresponde a uma coluna
# o valor dos índices é o valor que será definido na coluna passada em todas as linhas 
mapeados = map(dados, {'Breed' : 'Persa', 'Age_in_months' : '0'})

# group() recebe os dados e uma lista
# cada valor da lista é o nome de uma coluna que será usada para o agrupamento
# serão agrupados aqueles que possuírem valores iguais em todas as colunas enviadas como regra
agrupados = group(dados, ['Breed'])