# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelPropagation
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Simular um cenário semi-supervisionado rotulando apenas alguns pontos
rng = 42
random_unlabeled_points = rng.permutation(len(y))
num_unlabeled_points = 100
y[random_unlabeled_points[:num_unlabeled_points]] = -1  # Rotulando como -1 para indicar dados não rotulados

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de propagação de rótulos
label_propagation_model = LabelPropagation()

# Treinar o modelo
label_propagation_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = label_propagation_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Propagação de Rótulos: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))


# Neste exemplo, alguns dos rótulos no conjunto de dados são substituídos por -1 para simular dados não rotulados.
# O modelo de propagação de rótulos é então treinado nesses dados mistos. Este é apenas um exemplo básico, a escolha do modelo e a manipulação de dados semi-supervisionados podem variar dependendo do seu problema específico. -se de ajustar o código conforme necessário para o seu caso de uso.
