# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
#CALCULE SEU IMC E MOSTRE SEU STATUS,DE ACORDO COM A TABELA ABAIXO:
# ABAIXO DE 18.5: ABAIXO DO PESO.
# ENTRE 18.5 E 25: PESO IDEAL.
# 25 ATÉ 30 : SOBREPESO.
# 30  40  : OBESIDADE.
# ACIMA DE 40: OBESIDADE MORBIDA.

peso = float(input("Digite seu peso:(kg)"))
altura = float(input("Digite sua altura:(m)"))
imc = peso/(altura**2)
print("O IMC desse pessoa é {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif 25 > imc >= 18.5:
    print("Você está no peso ideal !")
elif 30 > imc >= 25:
    print(" Você está com sobrepeso.")
elif 40 > imc >= 30:
    print("Você está com obesidade.")
elif imc > 40:
    print("Você está com obesidade morbida")
else:
    print("Digite seu peso.")