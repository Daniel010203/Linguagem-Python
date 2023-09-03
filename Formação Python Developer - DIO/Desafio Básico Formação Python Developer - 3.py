# Função que verifica se B encaixa em A
def encaixa(A, B):
    # Verifica se o comprimento de B é maior que o de A
    if len(B) > len(A):
        return False

    # Compara os últimos dígitos de A com B
    for i in range(1, len(B) + 1):
        if A[-i] != B[-i]:
            return False

    return True


# Recebe a quantidade de casos de teste
N = int(input())

# Loop pelos casos de teste
for _ in range(N):
    # Recebe os valores A e B como strings
    A, B = input().split()

    # Verifica se B encaixa em A e imprime a mensagem correspondente
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa")
