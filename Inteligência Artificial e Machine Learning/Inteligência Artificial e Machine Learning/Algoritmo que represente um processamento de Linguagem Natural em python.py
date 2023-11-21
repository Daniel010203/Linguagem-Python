import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# Baixar recursos necessários (você só precisa fazer isso uma vez)
nltk.download('punkt')
nltk.download('stopwords')

# Texto de exemplo
sample_text = "Processamento de Linguagem Natural é fascinante! NLTK é uma ótima ferramenta para isso."

# Tokenização de palavras
tokens = word_tokenize(sample_text)

# Remoção de stopwords (palavras comuns que geralmente não contribuem para o significado)
stop_words = set(stopwords.words('portuguese'))  # Pode ser 'english' dependendo do idioma
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Contagem de frequência de palavras
fdist = FreqDist(filtered_tokens)

# Exibir palavras mais frequentes
print("Palavras mais frequentes:")
for word, freq in fdist.most_common(5):
    print(f"{word}: {freq} vezes")

