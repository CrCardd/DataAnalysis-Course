import tkinter as tk


class entity:
    def __init__(self, color):
        self.color = color
    
class wall(entity):
    def __init__(self):
        super().__init__('black')

class void(entity):
    def __init__(self):
        super().__init__('white')

class player(entity):
    def __init__(self, y, x):
        super().__init__('green')
        self.y = y
        self.x = x




matriz = [
    "WWWWWWWWWWWWWWW WWWWW",
    "W       W     W     W",
    "W W WWW W WWWWW WWW W",
    "W W W W W W     W W W",
    "W W W W W W WWWWW W W",
    "W W W W W   W     W W",
    "WWW W W WWW W WWW W W",
    "W   W W     W W W   W",
    "WWWWW WWW WWW W W W W",
    "W       W   W W   W W",
    "W WWWWW WWWWW WWW WWW",
    "W W   W       W W   W",
    "W WWW W WWWWWWW WWW W",
    "W     W W     W W   W",
    "WWW W W W WWW W WWW W",
    "W W W W W W W W   W W",
    "W W W WWW W W WWW WWW",
    "W W W     W W W W   W",
    "W WWW WWW W W W W W W",
    "W     W     W     W W",
    "WWWWWWW WWWWWWWWWWWWW",
]

matriz[20] = matriz[20].replace(' ', 'P')

TAMANHO = 40

CORES = {
    ' ': void(),
    'W': wall(),
    'P': player(20,7),
}

root = tk.Tk()
root.title("Labirinto")

canvas = tk.Canvas(root, width=len(matriz[0]) * TAMANHO, height=len(matriz) * TAMANHO)
canvas.pack()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        cor = CORES.get(matriz[i][j]).color
        x0 = j * TAMANHO
        y0 = i * TAMANHO
        x1 = x0 + TAMANHO
        y1 = y0 + TAMANHO
        canvas.create_rectangle(x0, y0, x1, y1, fill=cor, outline=cor)


root.mainloop()






# def check_move(key):

#     match key:
#         case 'w':
            
#         case 'a':
#         case 's':
#         case 'd':
