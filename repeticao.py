cont = 10

while cont >= 0:
     print(cont)
     cont = cont - 1

print("FOGO!")

cont = 0
senha = int(input("Digte sua senha:"))

while True:
     if senha == 1234:
         print("Seja bem vindo")
         break
     else:
         cont = cont + 1
         if cont < 3:
             print("Acesso negado")
             print(f"Você tem apenas {3 -cont } tentativas")
             senha = int(input("Tente novamente:"))
         else:
            print("Bloqueado")
            break

print("Fim")




    
