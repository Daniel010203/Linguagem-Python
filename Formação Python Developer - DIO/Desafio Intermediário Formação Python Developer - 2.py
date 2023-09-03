# Recebe o número de casos de teste
T = int(input())

# Loop pelos casos de teste
for _ in range(T):
    # Recebe N (número de refrigerantes comprados) e K (número de garrafas vazias para ganhar uma cheia)
    K, N = map(int, input().split())

    # Calcula o número de garrafas no primeiro dia
    garrafas_primeiro_dia = N
    # Calcula o número de garrafas no segundo dia
    garrafas_segundo_dia = N

    while garrafas_primeiro_dia >= K:
        # Calcula quantas garrafas vazias podem ser trocadas por cheias
        trocas = garrafas_primeiro_dia // K
        # Atualiza o número de garrafas no primeiro dia após as trocas
        garrafas_primeiro_dia = trocas + (garrafas_primeiro_dia % K)
        # Adiciona as garrafas ganhas ao total do segundo dia
        garrafas_segundo_dia += trocas

    # Imprime o número de garrafas no segundo dia
    print(garrafas_segundo_dia)
