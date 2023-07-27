#   ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
#CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# A VISTA DINHEIRO/CHEQUE:10% DE DESCONTO.
# A VISTA NO CARTÃO: 5% DE DESCONTO.
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL.
# 3X OU MAIS NO CARTÃO: 20% DE JUROS.
print(f"{' Lojas Daniel Oliveira.com ':=^40}")
valor_produto = float(input("Digite o valor do produto:R$ "))
print(""""FORMAS DE PAGAMENTO
[1] À VISTA NO DINHEIRO/CHEQUE
[2] À VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X NO CARTÃO""")
opção_pagamento = int(input("Qual será a opção da forma de pagamento? "))
if opção_pagamento == 1:
    total = valor_produto - (valor_produto * 10 / 100)
elif opção_pagamento == 2:
    total = valor_produto - (valor_produto * 5 / 100)
elif opção_pagamento == 3:
    total = valor_produto
    parcela = valor_produto / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif opção_pagamento == 4:
    total = valor_produto + (valor_produto*20/100)
    totalparcela = int(input("Quantas parcelas? "))
    parcela = total / totalparcela
    print(f"Sua compra será parcelada em {totalparcela:.2f} COM JUROS")
else:
    total = opção_pagamento
    print("OPÇÃO INVALIDA DE PAGAMENTO.TENTE NOVAMENTE !")
    print(f"Sua compra de R${valor_produto:.2f} vai custar R${valor_produto:.2f} no final")

