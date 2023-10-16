from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt

from ucimlrepo import fetch_ucirepo

training_accuracy = []
test_accuracy = []

kernels = ['linear', 'rbf', 'sigmoid']
for kernel in kernels:
    svm_
    model = svm.SVC(kernel=kernel)

    svm_model.fit(X_train_can, y_train_can)
    training_accuracy.append(svm_model.score(X_train_can, y_train_can))
    test_accuracy.append(svm_model.score(X_test_can, y_test_can))

plt.plot(kernels, training_accuracy, label='Acuracia no conj. treino')
plt.plot(kernels, test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Accuracy')
plt.xlabel('Kernels')
plt.legend()

training_accuracy = []
test_accuracy = []

prof_max = range(1,10)

for md in prof_max:
  tree = DecisionTreeClassifier(max_depth=md,random_state=0)
  tree.fit(X_train_can,y_train_can)
  training_accuracy.append(tree.score(X_train_can, y_train_can))
  test_accuracy.append(tree.score(X_test_can, y_test_can))

plt.plot(prof_max,training_accuracy, label='Acuracia no conj. treino')
plt.plot(prof_max,test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Acuracia')
plt.xlabel('Profundidade Maxima')
plt.legend()


training_accuracy = []
test_accuracy = []

for interception in [True, False]:
  regr = LinearRegression(fit_intercept=interception)
  regr.fit(X_train_dia, y_train_dia)
  training_accuracy.append(regr.score(X_train_dia, y_train_dia))
  test_accuracy.append(regr.score(X_test_dia, y_test_dia))

plt.plot(["Interc", "No Interc"],training_accuracy, label='Acuracia no conj. treino')
plt.plot(["Interc", "No Interc"],test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Acuracia')
plt.xlabel('Fit Intercept')
plt.legend()