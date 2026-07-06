convidados = []

while True:
    print("""Menu de opções
    1- Adicionar convidado
    2- Listar convidados
    3- Consultar convidado
    4- Remover convidados
    5- Quantidade de convidados
    6- Editar convidado
    0- Finalizar programa""")

    opcao = int(input("Digite a opção que você deseja:"))

    if opcao == 1:
        nome = input("Digite o nome do convidado que você deseja adicionar")
        convidados.append(nome)
        print("Convidado adicionado com sucesso!")

    elif opcao == 2:
        print("Lista de convidados")
        if not convidados:
            print("Nenhum convidado cadastrado na lista")
        else:
            for convidado in convidados:
                print(convidados)
        print()

    elif opcao == 3:
        pass



