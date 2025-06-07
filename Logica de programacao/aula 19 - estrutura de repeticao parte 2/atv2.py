import random as rd

def pacifista_para_zangado(pacifistas, zangados):
    return (pacifistas - 1, zangados + 1)
def zangado_para_pacifista(pacifistas, zangados):
    return (pacifistas + 1, zangados - 1)
def matar(alvos, dano):
    return (alvos - dano) if alvos - dano > 0 else 0

def guerra(pacifistas, zangados):
    pacifistas_original = pacifistas
    zangados_original = zangados

    zangados_dano = 1
    pacifistas_dano = 1

    print('INICIO:')
    print(f'Pacifistas:\t{pacifistas}\t| Zangados:\t{zangados}\n')
    while(pacifistas > 0 and zangados > 0):
        dado_pacifista = rd.randint(1,6)
        dado_zangado = rd.randint(1,6)

        evento = ''
        

        # ENLOQUECER
        if dado_pacifista == 1:
            pacifistas, zangados = pacifista_para_zangado(pacifistas, zangados)
            evento = 'O pacifista enlouqueceu e trocou de lado !'

        elif dado_pacifista == 6:
            pacifistas, zangados = zangado_para_pacifista(pacifistas, zangados)
            evento = 'O pacifista converteu o zangado !'
        
        elif dado_zangado == 6:
            pacifistas, zangados = zangado_para_pacifista(pacifistas, zangados)
            evento = 'O zangado enlouqueceu e trocou de lado !'

        elif dado_zangado == 2:
            zangados -= 1
            evento = 'O zangado enlouqueceu e se matou...'
        
        # EVENTOS ESPECIAIS
        elif dado_zangado == 1 and zangados < int(0.25 * zangados_original):
            zangados_dano *= 2
            evento = 'Os zangados entraram em fúria !!!!!'
        
        # CONFORONTO
        elif dado_zangado < dado_pacifista:
            zangados = matar(zangados, pacifistas_dano)
            evento = 'O pacifista derrotou o zangado !'
        elif dado_pacifista < dado_zangado:
            pacifistas = matar(pacifistas, zangados_dano)
            evento = 'O zangado derrotou o pacifista !'
        elif dado_pacifista == dado_zangado:
            pacifistas -= 1
            zangados   -= 1
            evento = 'Ambos se mataram...'

        print(f'Pacifistas:\t{pacifistas}\t| Zangados:\t{zangados}\t\t->\t{evento}')

    print('\nFIM !')
    print(f'Pacifistas:\t{pacifistas}\t| Zangados:\t{zangados}')

guerra(100,100)