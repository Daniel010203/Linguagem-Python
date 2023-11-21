# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Árvore de Decisão
decision_tree_model = DecisionTreeClassifier()

# Treinar o modelo
decision_tree_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = decision_tree_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Árvore de Decisão: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))

# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Árvore de Decisão
decision_tree_model = DecisionTreeClassifier()

# Treinar o modelo
decision_tree_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = decision_tree_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Árvore de Decisão: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))

#Neste exemplo, a árvore de decisão é treinada no conjunto de dados Iris para classificar as flores em três classes diferentes.
#Lembre-se de que a escolha do modelo e seus parâmetros depende do problema específico que você está resolvendo, e este exemplo serve como uma introdução básica ao uso de árvores de decisão em Python.