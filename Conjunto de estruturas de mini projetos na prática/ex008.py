#Escreva um programa que leia o valor em metros e o converta em centimetros e milimetros.
# se colocar {:.1f} faz com que tenhamos somente uma casa decimal após o ponto.
m = float(input("Digite a metragem: "))
c =  m*100
mi = c*1000
print("A medida de {:.1f}m corresponde a {:.1f}cm e {:.1f}mm".format(m,c,mi))

