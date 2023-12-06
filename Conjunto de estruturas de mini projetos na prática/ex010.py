#Crie um programa que leia quanto real a pessoa tem na carteira e mostre quantos dolares ela pode converter o real que possui.
valor = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = (valor/3.27) # valor do dólar no exemplo é $3.25
print("Com R${:.2f} voce pode comprar U$${:.2f}".format(valor,dolar))


#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um valor em reais e calcula quantos
#  dólares é possível comprar com esse valor, considerando que
#  o dólar vale R$3,27.
#----------------------------------------------------------------
#  Conversor de Moedas - Exercício #010
#----------------------------------------------------------------

r = float(input('Quantos reais você quer converter para US$?  R$'))
print(f'Com R${r:.2f} você pode comprar US${r/3.27:.2f}')


#CÓDIGO utilizado:
real = float(input("Quanto de real você possui na carteira ? R$ "))
dolar = (real/5.40) # valor do dola no exemplo é $5.40
print(f'Com R${real:.2f} você pode comprar US${real/5.40:.2f}')

# EXPLICAÇÃO DO CÓDIGO:
#O código selecionado solicita que o usuário insira a quantidade de dinheiro que possui em reais brasileiros (BRL) e depois o converte para dólares americanos (USD) usando uma taxa de câmbio fixa. Aqui está uma explicação passo a passo do código: 1. `real = float(input("Quanto de real você possui na carteira ? R$ "))` - Esta linha solicita que o usuário insira a quantidade de dinheiro que possui em BRL e armazena na variável `real`. A função `float()` é usada para converter a entrada do usuário em um número de ponto flutuante. 2. `dolar = (real/5,40)` - Esta linha calcula o valor equivalente em USD dividindo o valor em BRL (`real`) pela taxa de câmbio de 5,40. O resultado é armazenado na variável `dolar`. 3. `print(f'Com R${real:.2f} você pode comprar US${real/5.40:.2f}')` - Esta linha imprime o resultado da conversão. Ele utiliza uma string f para formatar a string de saída, exibindo o valor original em BRL (`real`) com 2 casas decimais (`:.2f`), e o valor equivalente em USD (`real/5,40`) também com 2 casas decimais (`:.2f`).
