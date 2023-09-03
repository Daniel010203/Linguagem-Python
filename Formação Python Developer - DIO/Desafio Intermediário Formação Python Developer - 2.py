T = int(input())
while T > 0:
    T -= 1
    N, K = input().split()
    N = int(N)
    K = int(K)
    total = int(int(N % K) + int(N / K))

    print(total)

# Processamento e saída para cada caso de teste
for _ in range(T):
    N, K = map(int, input().split())
    resultado = calcular_garrafas_segundo_dia(N, K)
    print(resultado)

