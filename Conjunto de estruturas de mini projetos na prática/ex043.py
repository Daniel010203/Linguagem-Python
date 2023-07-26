# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
#CALCULE SEU IMC E MOSTRE SEU STATUS,DE ACORDO COM A TABELA ABAIXO:
# ABAIXO DE 18.5: ABAIXO DO PESO.
# ENTRE 18.5 E 25: PESO IDEAL.
# 25 ATÉ 30 : SOBREPESO.
# 30  40  : OBESIDADE.
# ACIMA DE 40: OBESIDADE MORBIDA.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura
if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >=18.5 and <=25:
    print("Você está no peso ideal !")
elif imc >=25 and <=30:
    print(" Você está com sobrepeso.")
elif imc >=30 and <=40:
    print("Você está com obesidade.")
elif imc >40:
    print("Você está com obesidade morbida")
else:
    print("Digite seu peso.")