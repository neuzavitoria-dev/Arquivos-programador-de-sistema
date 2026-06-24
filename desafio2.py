rota_de_fuga = int(input("Rota de fuga opção 1(ponte da cidade) ou opção 2(tunel subterraneo): "))

if rota_de_fuga == 1:
    carro = input("Seu veiculo esta blindado: ")
    ponte = input("A ponte esta intacta:")
    if carro == "sim" and ponte == "sim":
        print("VENCEU")

    else:
        print("MORREU")

elif rota_de_fuga == 2:
    mascara = input("Você tem mascara de gás: ")
    cartao = input("Você tem cartão: ")
    if mascara == "sim" and cartao == "sim":
        print("VENCEU")

    else:print("MORREU")

else:
    print("Opção invalida, tente novamente.")


