numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    if ehVegano == 's':
        tipo = 'Vegano'

    elif ehVegano == 'n':
        tipo = 'Não-Vegano'

    print(f'Pedido {i}: {prato} ({tipo}) - {calorias} calorias')
