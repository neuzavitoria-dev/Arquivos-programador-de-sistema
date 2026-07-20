# def contar_vogais():
#     nome_arquivo = input("Digite o nome do arquivo texto:")
#     vogais = "aeiou"
#     total_vogais = 0
#     try:
#         with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
#             conteudo = arquivo.read().lower()
#             for caractere in conteudo:
#                 if caractere in vogais:
#                     total_vogais += 1
#         print(f"O arquivo possui {total_vogais} vogais.")
#     except FileNotFoundError:
#         print("O nome do arquivo não foi encontrado")

# contar_vogais()

def contar_caracter():
    nome_arquivo = input("Digite o nome do arquivo texto:")
    caracter = input("Digite o caracter a ser buscado no arquivo:")
    total_caracter = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for caractere in conteudo:
                if caractere in caracter:
                    total_caracter += 1
        print(f"O arquivo possui {total_caracter} vogais.")
    except FileExistsError:
        print("Erro: O arquivo não foi encontrado. Verifique o nome.")

contar_caracter()