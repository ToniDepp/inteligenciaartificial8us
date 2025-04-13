import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generamos datos sintéticos
np.random.seed(42)
X = np.random.randint(18, 60, (100, 2))  # Edad y salario (valores aleatorios)
y = np.random.choice([0, 1], size=100)  # 0: No compra, 1: Compra

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos y entrenamos el modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Hacemos predicciones
y_pred = modelo.predict(X_test)

# Evaluamos el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Visualización simple de los datos de prueba y sus predicciones
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k')
plt.xlabel('Edad')
plt.ylabel('Salario')
plt.title('Predicción de compra')
plt.show()