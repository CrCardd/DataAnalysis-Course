from lib import get_data

def filter(dados, coluna, comparaao):
    return None
            
def map(dados, coluna, modificacao):
    return None

def group(dados, coluna):
    return None



dados = get_data('./gatos.csv', ';')

filtrados = filter(dados, 'Breed', 'Maine coon')
mapeados = map(dados, 'Breed', 'Persa')
agrupados = group(dados, 'Breed')