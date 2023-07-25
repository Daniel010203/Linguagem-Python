#Código de reajuste salarial.
salario = float(input("Digite o salário do funcionário:R$  "))
novo_sala = salario + (salario * 15 / 100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento,vai passar a receber R${:.2f}".format(salario,novo_sala))

