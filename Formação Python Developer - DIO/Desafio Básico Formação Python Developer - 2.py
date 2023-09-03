# Lista com os nomes dos meses em inglês
meses = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Recebe a entrada do usuário como um número inteiro
numero_mes = int(input())

# Verifica se o número está dentro do intervalo válido (1 a 12)
if 1 <= numero_mes <= 12:
    # Obtém o nome do mês correspondente
    nome_mes = meses[numero_mes - 1]

    # Imprime o nome do mês com a primeira letra maiúscula
    print(nome_mes)
else:
    print("Número de mês fora do intervalo válido")
