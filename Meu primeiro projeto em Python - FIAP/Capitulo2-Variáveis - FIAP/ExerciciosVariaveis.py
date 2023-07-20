#Projeto para identificaçao de clientes uma empresa de ACADEMIA DE GINASTICA com nome de OLIVEIRAS FIT.
#*Categorias dos clientes: OURO,PRATA e BRONZE.
#*Tipo de Pacotes disponiveis : Completo,Especifico,Básico.
#Os valores dos pacotes são: OURO(100),PRATA(70) e BRONZE(40).
nomeCliente=input("Digite o nome do cliente: ")
categoria='OURO','PRATA','BRONZE'
tipoDePacotes='Completo','Especifico','Básico'
valoresPacotes=int(100),(70),(40)
nomeCategoriaCliente=input("Digite a categoria do cliente: ")
estadoDeLocalizacaoAcademia=input("Digite em qual Oliveiras Fit o(a) cliente está: ")
valorPacoteContratado=int(input("Digite qual o valor do pacote contratado pelo cliente: "))
tipoDePacoteContratado=input("Digite o tipo de pacote contratado: ")
if categoria=="BRONZE" or "PRATA":
    print("Pergunte se tem interesse em melhorar sua categoria atual para a OURO. Resposta sim ou não.")
mudarCategoria=input ("Podemos alterar seu pacote para OURO? ")
if mudarCategoria=="SIM":
    print ("ótimo, agradeça,entregue um brinde ao mesmo e parabenize o cliente pela escolhaSolicite os dados gerais para cadastro da nova categoria e informe os novos beneficios ao cliente.")
else:
    print("Ok, sua categoria atual também é ótimo e possui diversos serviços.Aproveite !")
if tipoDePacotes=="Completo" or "Especifico" or "Básico":
    print("Pergunte se o cliente tem interesse em mudar seu pacote de serviços na academia. Resposta sim ou não.")
tipoDePacotes=input("Gostaria então de melhorar seu pacote de serviços dentro de sua categoria atual? ")
if tipoDePacotes=="SIM":
    print("Solicite os dados para mudança de tipo de pacote e informe os novos beneficios do pacote ao cliente.")
else:
    print("Ok,seu pacote atual yambém é ótimo e possui doversos serviços.Aproveite !")
print("FIM")