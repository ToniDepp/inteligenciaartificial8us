from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
import pandas as pd

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo Naive Bayes
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# Realizar predicciones
predicciones = modelo.predict(X_test)

# Mostrar resultados
print("Precisión del modelo:", accuracy_score(y_test, predicciones))
print("\nReporte de clasificación:\n", classification_report(y_test, predicciones, target_names=data.target_names))
