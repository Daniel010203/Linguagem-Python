equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta =="S":
    equipamentos.append(input("Equipamento: "))
    valores.append((float(input("Valor: "))))
    seriais.append((int(input("Numero de serial: "))))
    departamentos.append((input("Departamento: ")))
    resposta = input('Digite \"S\" para continuar: ').upper()


for indice in range(0,len(equipamentos)):
    print("Equipamento..: ",(indice+1))
    print("Nome ......", equipamentos[indice])
    print("Valor......",valores[indice])
    print("Serial.....",seriais[indice])
    print("Departamento.",departamentos[indice])
    break

buscas=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if buscas==equipamentos[indice]:
        print("Valor ..: ",valores[indice])
        print("Serial..: ",seriais[indice])
        break

depreciacao = input("Degite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ",valores[indice])
        valores[indice] = valores[indice]* 0.9
        print("Novo valor: ",valores[indice])
        break

serial = int(input("Digite o serial do equipamento que será excluído: "))
for indice in range(0,len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]

for indice in range(0,len(equipamentos)):
    print("Equipamentos..: ",(indice+1))
    print("Valor....: ",equipamentos[indice])
    print("Serial ....: ",seriais[indice])
    print("Departamento ..: ",departamentos[indice])



