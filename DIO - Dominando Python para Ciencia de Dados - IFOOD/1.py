valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())
totHamburger = int(valorHamburguer * quantidadeHamburguer)
totBebida = int(valorBebida * quantidadeBebida)
totalCompra = int(totHamburger + totBebida)
troconecessario = float(valorPago - totalCompra)

print ("valorHamburguer =",valorHamburguer,";")
print ("quantidade=",quantidadeHamburguer,";")
print ("valorBebida=",valorBebida,";")
print ("valorPago=",valorPago,";")

print("O preço final do pedido é R${.:2} Seu troco é R${:.2}.".format(valorPago , troconecessario))

#rint("A medida de {:.1f}m corresponde a {:.1f}cm e {:.1f}mm".format(m,c,mi))