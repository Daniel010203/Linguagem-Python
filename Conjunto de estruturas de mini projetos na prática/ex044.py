#   ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
#CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# A VISTA DINHEIRO/CHEQUE:10% DE DESCONTO.
# A VISTA NO CARTÃO: 5% DE DESCONTO.
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL.
# 3X OU MAIS NO CARTÃO: 20% DE JUROS.

valor_produto = float(input("Digite o valor do produto: "))
formaDePagamento = str(input("Favor informe a forma de pagamento,conforme disponível na loja: "))
forma_pagamento_dinheiro_cheque = (valor_produto*20)/100
forma_pagamento_cartao = (valor_produto*5)/100
forma_pagamento_cartao2x = valor_produto
forma_pagamento_cartao3x = valor_produto + (valor_produto*20)/100
if forma_pagamento_dinheiro_cheque:
    print("Conceder desconto de 10%")
elif forma_pagamento_cartao:
    print(" Conceder desconto de 5%")
elif forma_pagamento_cartao2x:
    print("Preço normal")
elif forma_pagamento_cartao3x:
    print("Acrescentar 20% ao produto.")
else:
    print("Favor informe o valor do produto.")
