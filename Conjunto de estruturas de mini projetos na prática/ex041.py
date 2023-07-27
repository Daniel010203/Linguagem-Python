# A COMFEDERAÇAO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA
# E MOSTRE SUA CATEGORIA, DE ACORDO COM SUA IDADE:
# ATÉ 9 ANOS : MIRIM
# ATÉ 14 ANOS : INFANTIL
# ATÉ 19 ANOS : JUNIOR
# ATÉ 20 ANOS : SENIOR
# ACIMA DE 25 ANOS : MASTER
from datetime import date
ano_atual=date.today().year
ano_nascimento = int(input("Digite o ano do nascimento: "))
idade_atleta = ano_atual - ano_nascimento # sempre faça o calculo com o ano atual na frente.
print("O atleta tem {} anos".format(idade_atleta))
if idade_atleta <= 9:
    print("Mirim")
elif idade_atleta <= 14:
    print("Infantil")
elif idade_atleta <= 19:
    print("Junior")
elif idade_atleta <= 20:
    print('Senior')
elif idade_atleta > 25:
    print("Master")
else:
    print("Digite a idade correta.")