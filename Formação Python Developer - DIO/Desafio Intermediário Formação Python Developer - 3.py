# Lê as três palavras
palavra1 = input()
palavra2 = input()
palavra3 = input()

# Define um dicionário para mapear as palavras para os animais
mapeamento = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

# Encontra o animal correspondente no dicionário
animal = mapeamento.get(palavra1, {}).get(palavra2, {}).get(palavra3, "desconhecido")

# Imprime o resultado
print(animal)
