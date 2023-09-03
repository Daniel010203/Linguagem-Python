opcao = 1

while opcao !=0:
    opcao = int(input("[1] sacar \n[2] extrato \n sair \n: "))

    if opcao == 1:
        print("Sacando....")
    elif opcao ==2:
        print("Exibindo o contrato ....")
else:
    print("Obrigado por utilizar o sistema.")