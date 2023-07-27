#CRIE UM PROGRAMA QUE LEIA AS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA ,MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA.
# MÉDIA ABAIXO DE 5.0 = REPROVADO.
# MÉDIA 5.0 E 6.9 = RECUPERAÇÃO.
# MÉDIA 7.0 = APROVADO
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2
print("Alcançando a nota {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota_1,nota_2,media))
if media < 5.0:
    print("Reprovado")
elif 7.0 > media >= 5.0:
    print("Recuperação")
elif 10.0 > media >= 7.0:
    print("Aprovado")
else:
    print("Está média não está correta,por favor digite as notas entre 0.0 e 10.0")
