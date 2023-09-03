print(True and True)
print(True and False)
print(True or True)
print(True or False and True)
print(True or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp_3 = conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(exp_3)