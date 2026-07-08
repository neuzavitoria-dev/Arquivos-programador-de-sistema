#Calculadora
def numeros():
    num1 = float(input("Digite o primeiro numero:\n "))
    num2 = float(input("Digite o segundo numero:\n "))
    return num1, num2

def soma(a, b):
     resultado = a + b
     print(f"O resultado da soma é: {resultado}\n")


def subtracao(a, b):
     resultado = a - b
     print(f"O resultado da subtração é: {resultado}\n")

def multiplicacao(a, b):
     resultado = a * b
     print(f"O resultado da multiplicação é: {resultado}\n")

def divisao(a, b):
    if b != 0:
         resultado = a / b
         print(f"O resultado da divisão é: {resultado}\n")
    else:
        print("Erro: Divisão por zero não é permitida.\n")

def menu():
     while True:
         print("""Escolha uma das opções abaixo:
             1 - Soma
             2 - Subtração
             3 - Multiplicação
             4 - Divisão
             5 - Sair\n""")
         opcao = input("Digite a opção desejada:\n ")

         if opcao == "1":
             n1, n2 = numeros()
             soma(n1, n2)
         elif opcao == "2":
             n1, n2 = numeros()
             subtracao(n1, n2)
         elif opcao == "3":
             n1, n2 = numeros()
             multiplicacao(n1, n2)
         elif opcao == "4":
             n1, n2 = numeros()
             divisao(n1, n2)
         elif opcao == "5":
             print("Saindo do programa...\n")
             break
         else:
             print("Opção inválida. Tente novamente.\n")

menu()

#Atividades
def numeros( n1, n2, n3):
     for i in range(3):
         numero = float(input("Digite um numero: "))
     soma = numero + numero + numero
     print(f"A soma dos numeros é:{soma}")

numeros()



