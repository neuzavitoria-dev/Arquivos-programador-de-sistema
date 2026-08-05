import tkinter as tk
import tkinter.messagebox as messagebox

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == user_name and senha == senha_admin:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")
#login admin
user_name = "admin"
senha_admin = "admin123"

#Criar janela principal
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x250")
janela.resizable(False, False)
frame_login = tk.Frame(janela)
frame_login.pack(expand=True)

# Título
label_titulo = tk.Label(frame_login, text="Sistema de Login", font=("Arial", 16))
label_titulo.pack(pady=10)

# Usuário
label_usuario = tk.Label(frame_login, text="Usuário:")
label_usuario.pack(pady=5)

entry_usuario = tk.Entry(frame_login)
entry_usuario.pack(pady=5)

# Senha
label_senha = tk.Label(frame_login, text="Senha:")
label_senha.pack(pady=5)

entry_senha = tk.Entry(frame_login, show="*")
entry_senha.pack(pady=5)

# Botão
botao_login = tk.Button(frame_login, text="Login", command=fazer_login)
botao_login.pack(pady=10)

janela.mainloop()