from time import sleep
print("##"*15)
print("Bem Vindo ao LGBank")
print("##"*15)
saldo = 0
limite_diario = 3
numero_saques = 0
saques_negado = 0
total_saque = 0

def menu():
    sleep(1)
    print("##"*15)
    print("Escolha uma das opções abaixo")
    print("##"*15)
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Encerrar")
    print("##"*15)

while True:
    menu()
    opcao = input("Digite uma Opção! ")

    if opcao == '1':
        while True:
            deposito = input("Quanto Deseja Depositar? ")
            if deposito.isdigit():
                saldo += float(deposito)
                print("Processando Depósito...")
                sleep(2)
                print("##"*15)
                print("Depósito Feito Com Sucesso")
                print(f"Seu Saldo Atual é R${saldo:.2f}")
                print("##"*15)
                break
            else:
                print("Valor não permitido. Por favor, digite apenas números.")

    elif opcao == '2':
        if numero_saques < limite_diario:
            retira = input("Quanto Deseja Sacar? ")
            if retira.isdigit():
                retira = float(retira)
                if retira <= saldo:
                    saldo -= retira
                    total_saque += retira
                    numero_saques += 1
                    print("Aguarde Estamos Processando Saque...")
                    sleep(2)
                    print("##"*25)
                    print(f"Saque Realizado Com Sucesso No Valor de R${retira:.2f}")
                    print(f"Seu Saldo Atual é R${saldo:.2f}")
                    print("##"*25)
                else:
                    print("_-*"*10)
                    print(f"Seu saldo atual é de R${saldo:.2f}")
                    print(f"Você está tentando sacar R${retira:.2f}")
                    print("Não é possível realizar o saque. Valor do Saque Maior Que Saldo Atual")
                    print("_-*"*10)
            else:
                print("Saque Não permitido. Você precisa digitar apenas números.")
        else:
            print("Você atingiu o limite de saque diário.")

    elif opcao == '3':
        print("##"*15)
        print("Seu Extrato")
        print("##"*15)
        print(f"Seu Saldo é de R${saldo:.2f}")
        print(f"Você realizou {numero_saques - saques_negado} saques")
        print(f"Total Sacado: R${total_saque:.2f}")
        print("##"*15)

    elif opcao == '4':
        print("Estamos finalizando sua sessão...")
        sleep(2)
        print("Sessão Finalizada Com Sucesso.")
        break

    else:
        print("Opção Inválida. Por favor, digite uma opção válida.")
