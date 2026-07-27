import sqlite3

# CONECTAR AO BANCO DE DADOS (OU CRIAR UM NOVO)
conexao = sqlite3.connect('exemplo.db')
# CRIAR UM CURSOR PARA INTERAGIR COM O BANCO DE DADOS
cursor = conexao.cursor()
# CRIAR A TABELA ALUNOS
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(
    ID INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
''')
# CONFIRMA A TRANSAÇÃO
conexao.commit()

def dadosAluno(nome,idade,curso):
    cursor.execute('''INSERT INTO Alunos (nome, idade, curso)
    VALUES (?, ?, ?)''')

conexao.commit()

def aluno():
    nome = input("Qual nome do aluno: ")
    idade =int(input("Digite a idade do aluno: "))
    curso = input("Qual   o curso do aluno: ")