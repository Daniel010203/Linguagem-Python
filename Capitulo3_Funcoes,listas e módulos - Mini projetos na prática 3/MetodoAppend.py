inventario = []
resposta = "S"
while resposta =="S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append((int(input("Número Serial: "))))
    inventario.append(input("Departamento: "))
    resposta = input("Deseja outras informações sobre a lista no inventário?")
for elemento in inventario:
    print(elemento)
