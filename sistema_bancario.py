menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

>= """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
     
     opcao = input(menu)
     
     if opcao == "a":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado não é suficiente. ")
        
        
     elif opcao == "b":
          
          valor = float(input("Digite o valor a ser sacado: "))
          
          excedeu_saldo = valor > saldo

          excedeu_limite = valor > LIMITE

          excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        
          if excedeu_saldo:
               print("Operação falhou! Você não têm saldo suficiente. ")

          elif excedeu_limite:
               print("Operação falhou! O valor do saque excede o liminte. ")

          elif excedeu_saques:
               print("Operação falhou! O Número máximo de saques excedido. ")

          elif valor > 0:
               saldo -= valor
               extrato += f"Saque: R$ {valor: .2f}\n"
               numero_saques += 1

          else:
              print("Operação falhou! Valor informado inválido. ")
        
        
     elif opcao == "c":
         print("**********EXTRATO**********")
         print("Não foram realizadas movimentações. " if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("***************************")

     elif opcao == "d":
        break

      
     else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
