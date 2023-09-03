# Recebe a entrada do usuário
texto = input()

# Verifica o comprimento do texto
if len(texto) <= 140:
    print("TWEET")
else:
    print("MUTE")