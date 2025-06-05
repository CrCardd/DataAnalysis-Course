import tkinter as tk

# Variável de controle de movimento contínuo
movendo = {"w": False, "a": False, "s": False, "d": False}

# Função de movimento
def mover():
    dx = dy = 0
    if movendo["w"]: dy -= 5
    if movendo["s"]: dy += 5
    if movendo["a"]: dx -= 5
    if movendo["d"]: dx += 5

    if dx != 0 or dy != 0:
        canvas.move(jogador, dx, dy)

    root.after(30, mover)  # repete a função a cada 30ms

# Tecla pressionada
def pressionar_tecla(event):
    tecla = event.keysym.lower()
    if tecla in movendo:
        movendo[tecla] = True

# Tecla liberada
def soltar_tecla(event):
    tecla = event.keysym.lower()
    if tecla in movendo:
        movendo[tecla] = False

# Criação da janela
root = tk.Tk()
root.title("Controle com W A S D")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

jogador = canvas.create_rectangle(180, 180, 220, 220, fill="blue")

# Bind de eventos
root.bind("<KeyPress>", pressionar_tecla)
root.bind("<KeyRelease>", soltar_tecla)

# Inicia o loop de movimento
mover()

root.mainloop()
