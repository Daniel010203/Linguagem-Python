#CRIE UM PROGRAMA QUE LEIA AS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA ,MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA.
# MÉDIA ABAIXO DE 5.0 = REPROVADO.
# MÉDIA 5.0 E 6.9 = RECUPERAÇÃO.
# MÉDIA 7.0 = APROVADO
nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2)/2
if media < 5.0:
    print("Reprovado")
elif media >=5.0:
    print("Recuperação")
elif media <=6.9:
    print("Recuperação")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Digite uma nota entre 0.0 e 10.0")
