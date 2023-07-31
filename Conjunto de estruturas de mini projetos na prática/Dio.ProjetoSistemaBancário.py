print(
    "Olá,seja muito bem vindo ao nosso Banco X,gostariamos de convida-lo a acessar as informações de sua conta bancária,ok !")
print("Embarque nessa conosco !!!")
usuario = str(input("Seja muito bem vindo, para começar,por favor digite seu nome completo: "))
deposito_1 = int(input("Digite quanto deseja depositar agora : "))
deposito_2 = int(input("Digite quanto foi depositado todo o dia de ontem: "))
saldo = deposito_2 + deposito_1
print("Sua conta possui :R$ ",saldo," disponível para saque.")