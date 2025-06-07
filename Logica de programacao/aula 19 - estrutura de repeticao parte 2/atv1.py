import random as rd

game = [
    None,None,None,
    None,None,None,
    None,None,None
]

ganhador = False
for _ in range(5):
    
    for i in range(3):
        for j in range(3):
            print(f' {game[i*3+j] if game[i*3+j] != None else f'({i*3+j})'} ', end='   ')
        print('\n')

    jogada = ''
    valido = False
    while (not valido):
        jogada = input("Digite a posição que deseja jogar ->   ")

        if jogada.isnumeric() and int(jogada) < len(game) and game[int(jogada)] == None : 
            valido = True
    jogada = int(jogada)
    game[jogada] = ' X '
    
    possibilidades = [i for i in range(9) if game[i] == None]
    if int(len(possibilidades)):
        game[possibilidades[rd.randint(0,len(possibilidades)-1)]] = ' O '



