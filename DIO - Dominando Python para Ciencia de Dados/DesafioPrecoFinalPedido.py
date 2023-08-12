valorHamburguer = float(input("Por favor,digite o valor do hamburguer: "))
quantidadeHamburguer = int(input("Por favor,digite quantos hamburgueres deseja comprar: "))
valorBebida = float(input("Digite quantas bebidas deseja comprar: "))
quantidadeBebida = int(input("Digite quanto custa a bebida que deseja comprar: "))
valorPago = float(input("Digite o valor das bebidas que deseja comprar: "))
precoFinalPedido = float(quantidadeHamburguer*valorHamburguer)+(quantidadeBebida*valorBebida)
troconecessario = float(valorPago-precoFinalPedido)

print("O preço final do pedido é R$",precoFinalPedido," Seu troco é R$",troconecessario,".")

#no sistema DIO.
alorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())
totHamburger = valorHamburguer * quantidadeHamburguer
totBebida = valorBebida * quantidadeBebida
totalCompra = totHamburger + totBebida
troconecessario = valorPago - totalCompra

print("O preço final do pedido é R$",valorPago," Seu troco é R$",troconecessario,".")