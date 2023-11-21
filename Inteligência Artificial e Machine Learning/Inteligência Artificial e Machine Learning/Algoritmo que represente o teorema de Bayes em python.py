#O teorema de Bayes é uma fórmula fundamental em probabilidade condicional. Vou fornecer um exemplo simples em Python para ilustrar como você pode implementar o teorema de Bayes em um contexto de classificação. Neste exemplo, usaremos o teorema de Bayes ingênuo (Naive Bayes) para classificar o texto como positivo ou negativo:

class NaiveBayesClassifier:
    def __init__(self, positive_prob, negative_prob):
        self.positive_prob = positive_prob
        self.negative_prob = negative_prob

    def classify(self, text):
        # Aplicar o Teorema de Bayes
        evidence = text.split()
        positive_likelihood = self.calculate_likelihood(self.positive_prob, evidence)
        negative_likelihood = self.calculate_likelihood(self.negative_prob, evidence)

        # Classificar com base nas probabilidades calculadas
        if positive_likelihood > negative_likelihood:
            return "Positivo"
        else:
            return "Negativo"

    def calculate_likelihood(self, prior_prob, evidence):
        likelihood = prior_prob  # Inicializar com a probabilidade priori

        # Simplesmente multiplicar as probabilidades de cada palavra no texto
        for word in evidence:
            likelihood *= self.word_probability(word)

        return likelihood

    def word_probability(self, word):
        # Probabilidades condicionais fictícias para ilustração
        positive_word_prob = 0.8
        negative_word_prob = 0.2

        # Supondo que as palavras são independentes (Naive Bayes)
        return positive_word_prob if word in ["good", "excellent"] else negative_word_prob

# Exemplo de uso
positive_prior_prob = 0.5
negative_prior_prob = 0.5

classifier = NaiveBayesClassifier(positive_prior_prob, negative_prior_prob)

# Texto de exemplo a ser classificado
input_text = "This movie is excellent and highly recommended."

# Classificar o texto
classification_result = classifier.classify(input_text)
print(f"A classificação do texto é: {classification_result}")

#Este é um exemplo muito simplificado para ilustrar a aplicação do teorema de Bayes ingênuo em uma tarefa de classificação de texto. Em um cenário real, você precisaria de dados mais complexos e probabilidades mais precisas para obter resultados significativos.