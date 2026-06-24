nave_pouso = input("Quantos porcentos está o combustivel da nave: ")
atmosfera = input("O ar dessa atmosferan é respirável: ")
traje = input("Quantos porcentos esta o traje da tribulação: ")

if nave_pouso >= "15" and (atmosfera == "sim" or traje == "100"):
    print("Iniciando Protocolo de Pouso.")
else:
    print("Pouso Abortado:Risco de Morte.")