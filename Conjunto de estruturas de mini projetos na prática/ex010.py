#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.
valor = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = (valor/3.27) # valor do dólar no exemplo é $3.25
print("Com R${:.2f} voce pode comprar U$${:.2f}".format(valor,dolar))
