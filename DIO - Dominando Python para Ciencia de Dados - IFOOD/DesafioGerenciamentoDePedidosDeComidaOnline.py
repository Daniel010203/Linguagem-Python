class Pedido:
    def __init__(self, valor):
        self.valor = valor
class SistemaPedidos:
    def __init__(self):
        self.pedidos = []
        self.desconto = 0.0

    def adicionar_pedido(self, valor):
        novo_pedido = Pedido(valor)
        self.pedidos.append(novo_pedido)

    def escolher_desconto(self, opcao):
        if opcao == 1:
            self.desconto = 0.1
        elif opcao == 2:
            self.desconto = 0.2
        else:
            print("Opção de desconto inválida.")

    def calcular_valor_total(self):
        valor_total = sum(pedido.valor for pedido in self.pedidos)
        valor_total_com_desconto = valor_total * (1 - self.desconto)
        return valor_total_com_desconto

# Função auxiliar para obter a opção do usuário
def obter_opcao():
    print("Escolha uma opção:")
    print("1. Adicionar pedido")
    print("2. Escolher desconto")
    print("3. Calcular valor total com desconto")
    print("4. Sair")
    return int(input())

# Função principal
def main():
    sistema = SistemaPedidos()

    while True:
        opcao = obter_opcao()

        if opcao == 1:
            valor_pedido = float(input("Digite o valor do pedido: "))
            sistema.adicionar_pedido(valor_pedido)
        elif opcao == 2:
            print("Escolha um cupom de desconto:")
            print("1. 10% de desconto")
            print("2. 20% de desconto")
            cupom = int(input())
            sistema.escolher_desconto(cupom)
        elif opcao == 3:
            valor_total_com_desconto = sistema.calcular_valor_total()
            print("Valor total com desconto: R$", valor_total_com_desconto)
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
