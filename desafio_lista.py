# DESAFIO 1
numeros_interios = [0,1, 2, 3, 4, 5, 6, 22, 35, 50]
nova_lista = []

for i in numeros_interios:
    if i % 2 == 0:
        nova_lista.append(0)
    else:
         nova_lista.append(i)
        
print(numeros_interios)
print(nova_lista)

# DESAFIO 2

numero = []
pares = []
impares = []

for i in range(20):

    numeros = int(input(f"Digite o {i+1}º numero inteiro:"))
    numero.append(numeros)

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print("lista de numeros inteiros",(numero))
print("lista de numeros par",(pares))
print("lista de numeros impares",(impares))









