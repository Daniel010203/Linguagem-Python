# Função para calcular o número de garrafas no segundo dia
def calcular_garrafas_segundo_dia(N, K):
    garrafas = N  # Inicialmente, o cliente tem N garrafas

    while N >= K:
        trocas = N // K  # Calcula o número de trocas possíveis
        garrafas += trocas  # Adiciona as garrafas obtidas nas trocas
        N = trocas + (N % K)  # Atualiza o número de garrafas vazias

    return garrafas

# Leitura do número de casos de teste
T = int(input())

# Processamento e saída para cada caso de teste
for _ in range(T):
    N, K = map(int, input().split())
    resultado = calcular_garrafas_segundo_dia(N, K)
    print(resultado)

