valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())
totHamburger = quantidadeHamburguer * valorHamburguer #R$8
totBebida = valorBebida * quantidadeBebida
totalCompra = totBebida + totHamburger
troconecessario = valorPago - totalCompra

print(f"O preço final do pedido é R${totalCompra:.2f}.Seu troco é de R${troconecessario:.2f}")