conta_normal = True
conta_universitaria = False

saldo = 4000
saque = 4000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso !")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do limite do cheque especial.")
    else:
        print("Saldo insuficiante.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso !")
    else:
        print("Saldo insuficiente.")
else:
    print("Sistema não reconheceu seu tipo de conta.")