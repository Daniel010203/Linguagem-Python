# Exemplo simples de aprendizado não supervisionado usando o algoritmo K-Means. Neste exemplo, usaremos a biblioteca scikit-learne o conjunto de dados Iris:

# Importar bibliotecas
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data

# Criar o modelo K-Means com 3 clusters (porque sabemos que o conjunto de dados Iris tem 3 classes)
kmeans_model = KMeans(n_clusters=3, random_state=42)

# Treinar o modelo
kmeans_model.fit(X)

# Obter rótulos dos clusters e centróides
labels = kmeans_model.labels_
centroids = kmeans_model.cluster_centers_

# Visualizar os resultados
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=3, color='r')
plt.title('Clusters identificados pelo K-Means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

#Neste exemplo, o algoritmo K-Means é aplicado ao conjunto de dados Iris para agrupar os dados em três clusters.
# O código inclui uma visualização simples dos clusters e seus centróides no espaço bidimensional das duas primeiras características do conjunto de dados.
