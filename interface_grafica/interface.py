import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Tkinter!")

# Rotulo simples

label = tk.Label(janela, text="Bem vindo ao sistema!")
label2 = tk.Label(janela, text="Olá vitoria!")
label.pack()
label2.pack()

# Inicio do loop principal
janela.mainloop()