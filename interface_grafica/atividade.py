import tkinter as tk
import sqlite3
janela = tk.Tk()
janela.title("Componentes Básicos")

#######################label nome e caixa de texto nome #########################

label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

#######################label idade e caixa de texto idade #########################

label_idade = tk.Label(janela, text="Digite sua idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

#######################label curso e caixa de texto curso #########################

label_curso = tk.Label(janela, text="Digite seu curso:")
label_curso.pack()
entry_curso = tk.Entry(janela)
entry_curso.pack()

#######################label email e caixa de texto email #########################

label_email = tk.Label(janela, text="Digite seu email:")
label_email.pack()
entry_email = tk.Entry(janela)
entry_email.pack()



def exibir_nome():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    curso = entry_curso.get()
    email = entry_email.get()

    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Idade INTEGER,
        Curso TEXT 
    )''')
    conexao.commit()
    cursor.execute("INSERT INTO Alunos (Nome, Idade, Curso, Email) VALUES (?, ?, ?, ?)", (nome, idade, curso, email))
    conexao.commit()
   


button = tk.Button(janela, text="Enviar", command=exibir_nome)
button.pack()

janela.mainloop()


conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()
cursor.execute('''ALTER TABLE Alunos ADD COLUMN Email TEXT;''')
conexao.commit()
