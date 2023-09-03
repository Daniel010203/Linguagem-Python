maior_idade = 18
idade_especial = 17
idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Ele poderá tirar a CNH.")
elif idade < maior_idade:
    print("Ainda não pode tirar a CNH.")

if idade >= maior_idade:
    print("Maior de idade,pode tirar a CNH.")
elif idade == idade_especial:
    print("Ele(a) pode fazer a aula teórica somente.")
else:
    print("Ainda não pode tirar a CNH.")


