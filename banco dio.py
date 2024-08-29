print('-' * 40)
print("Ola seja bem vindo ao Banco".center(40))
print('-' * 40)

menu = ("""        Escolha uma opção

       1 - Deposito
       2 - Saque 
       3 - Extrato    
       4 - sair

      """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opçao = input(menu)
    if opçao == "1":
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor:.2f} \n"
            print("Deposito realizado com sucesso!")
        else:
            print("Valor invalido. Tente novamente.")


    elif opçao == "2":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        if excedeu_saldo:
            print('operaçao falhou! Saldo insuficiente.')
        elif excedeu_limite:
            print("operaçao falhou! Limite de saque excedido.")
        elif excedeu_saques:
            print("operaçao falhou! Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f} \n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("operação falhou valor informando é invalido ")

    elif opçao == "3":
        print('\n ==============Extrato=============')
        print('nao foram realizadas movimentaçoes' if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")

        print("=======================================")
    elif opçao == "4":
        print("obrigado por usar nosso banco ate logo")
        break
    else:
        print("opção invalida. por favor Tente novamente a operação.")
