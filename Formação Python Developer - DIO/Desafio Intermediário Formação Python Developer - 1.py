# Recebe o número de casos de teste
C = int(input())

# Loop pelos casos de teste
for _ in range(C):
    # Recebe o nível de energia como entrada
    N = int(input())

    # Verifica se o nível de energia é menor ou igual a 8000 e imprime a mensagem correspondente
    if N <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")
