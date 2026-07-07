convidados = []

while True:
    print("""Menu de opções
    1- Adicionar convidado
    2- Listar convidados
    3- Consultar convidado
    4- Remover convidados
    5- Quantidade de convidados
    6- Editar convidado
    0- Finalizar programa\n""")

    opcao = int(input("Digite a opção que você deseja:"))

    if opcao == 1:
        nome = input("Digite o nome do convidado que você deseja adicionar: ")
        convidados.append(nome)
        print(f"Convidado {nome} adicionado com sucesso!\n")

    elif opcao == 2:
        print("Lista de convidados.\n")
        if not convidados:
            print("Nenhum convidado cadastrado na lista.\n")
        else:
            for convidado in convidados:
                print(convidado)

    elif opcao == 3:
        nome = input("Digite o nome do convidado que você consulta: ")
        if nome in convidados:
            for convidado in convidados:
                if convidado == nome:
                    print(f"Convidado encontrado:{convidado}\n")
        else:
            print("Convidado não encontrado.\n")

    elif opcao == 4:
        nome = input("Digite o nome do convidado que você deseja remover: ")
        if nome in convidados:
            convidados.remove(nome)
            print(f"Convidado {nome} removido com sucesso!\n")
        else:
            print("Este convidado {nome} não esta na lista.\n")

    elif opcao == 5:
        print("Quantidade de convidados da lista é:", len(convidados))

    elif opcao == 6:
        nome_atual = input("Digite o nome do convidado que você deseja editar: ")
        if nome_atual in convidados:
            novo_nome = input("Digite o novo nome do convidado:")
            index = convidados.index(nome_atual)
            convidados[index] = novo_nome

            print(f"Convidado {nome_atual} atualizado para {novo_nome} com sucesso!\n")
        else:
            print("Convidado não encontrado.\n")

    elif opcao == 0:
        print("Programa finalizado.\n")
        break

    else:
        print("Opção invalida, tente novamente outra opção.\n")

            

        



