#Criação de um estoque de loja
# estoque = {
#     "Arroz": 50,
#     "Feijao": 35,
#     "Macarrao": 40,
#     "Acucar": 0,
#     "Sal": 30,
#     "Oleo": 18,
#     "Cafe": 22,
#     "Leite":0,
#     "Manteiga": 15,
#     "Queijo": 12,
#     "Pao": 60,
#     "Biscoito": 28,
#     "Refrigerante": 20,
#     "Agua Mineral": 55,
#     "Sabao em Po": 0,
#     "Detergente": 24,
#     "Shampoo": 14,
#     "Condicionador": 0,
#     "Papel Higienico": 32,
#     "Creme Dental": 26
# }

# def consultar_produto():
#     produto = input("Digite o nome do produto que você deseja consultar em estoque: ").title()

#     if produto in estoque:
#         if estoque[produto] == 0:
#             print(f"O produto {produto} está sem estoque.")
#         else:
#             print(f"Produto {produto} encontrado!")
#             print(f"Quantidade em estoque: {estoque[produto]}")
#     else:
#         print("Produto não encontrado.")

# consultar_produto()

#Tradução das palavras em ingles para o portugues
    
dicionario_ingles ={
    "House": "Casa",
    "Car": "Carro",
    "Book": "Livro",
    "Dog": "Cachorro",
    "Cat": "Gato",
    "School": "Escola",
    "Computer": "Computador",
    "Phone": "Telefone",
    "Water": "Agua",
    "Food": "Comida",
    "Chair": "Cadeira",
    "Table": "Mesa",
    "Window": "Janela",
    "Door": "Porta",
    "Tree": "Arvore",
    "Flower": "Flor",
    "Sun": "Sol",
    "Moon": "Lua",
    "Friend": "Amigo",
    "Teacher": "Professor",
    "Student": "Estudante",
    "Pen": "Caneta",
    "Pencil": "Lapis",
    "Notebook": "Caderno",
    "Bag": "Mochila",
    "Bottle": "Garrafa",
    "Milk": "Leite",
    "Coffee": "Cafe",
    "Bread": "Pao",
    "Rice": "Arroz",
    "Bean": "Feijao",
    "Sugar": "Acucar",
    "Salt": "Sal",
    "Cheese": "Queijo",
    "Butter": "Manteiga",
    "Fish": "Peixe",
    "Chicken": "Frango",
    "Meat": "Carne",
    "Fruit": "Fruta",
    "Apple": "Maca",
    "Banana": "Banana",
    "Orange": "Laranja",
    "Grape": "Uva",
    "Strawberry": "Morango",
    "Juice": "Suco",
    "Egg": "Ovo",
    "Kitchen": "Cozinha",
    "Bathroom": "Banheiro",
    "Bedroom": "Quarto",
    "Garden": "Jardim"
}

def traducao():
    palavra = input("Digite a palavra que você quer traduzir:").title()

    if palavra in dicionario_ingles:
            print(f"A tradução de {palavra} é: {dicionario_ingles[palavra]}")
    else:
        print("Palavra não encontrada no dicionário.")

def adicionar_palavra():
    nova_palavra = input("Digite a palavra em inglês que você deseja adicionar: ").title()
    nova_traducao = input("Digite a tradução da palavra: ").title()

    if nova_palavra in dicionario_ingles:
        print("Essa palavra já existe no dicionário.")
    else:
        dicionario_ingles[nova_palavra] = nova_traducao
        print("Palavra adicionada com sucesso!")

    
while True:
    print("""Dicionario inglês-portugues
        1 - Busca tradução
        2 - Adicionar palavra
        3 - Sair
           """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
         print(traducao())

    elif opcao == "2":
         print(adicionar_palavra())
    
    elif opcao == "3":
         print("Saindo do programa...")
         break
    else:
         print("Opção invalida, tente novamente outra opção.")
     
