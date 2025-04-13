import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Datos de jugadores (Goles, Asistencias, Partidos Ganados, Partidos Perdidos)
X = np.array([
    [1, 1, 2, 3], [0, 0, 1, 4], [2, 1, 3, 1], [0, 1, 1, 3],
    [3, 2, 5, 0], [4, 3, 6, 1], [0, 0, 0, 5], [1, 2, 2, 2],
    [5, 4, 8, 0], [2, 3, 3, 2]
])

# Etiquetas de desempeño (0: Mal jugador, 1: Posible venta, 2: Se mantiene, 3: Buen jugador, 4: Excelente jugador)
y = np.array([1, 0, 2, 1, 3, 4, 0, 2, 4, 3])

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Clasificación de nuevos jugadores
niveles = ["Mal jugador", "Posible venta", "Se mantiene una temporada más", "Buen jugador", "Excelente jugador"]
print("<----- Jugador Uno ----->")
nuevo_jugador = np.array([[3, 2, 4, 1]])
prediccion = modelo.predict(nuevo_jugador)[0]
print(f'El nuevo jugador es: {niveles[prediccion]}')
print("<----- Jugador Dos ----->")
nuevo_jugador_dos = np.array([[0, 0, 1, 4]])
prediccion = modelo.predict(nuevo_jugador_dos)[0]
print(f'El nuevo jugador es: {niveles[prediccion]}')
print("<----- Jugador Tres ----->")
nuevo_jugador_tres = np.array([[15, 10, 7, 3]])
prediccion = modelo.predict(nuevo_jugador_tres)[0]
print(f'El nuevo jugador es: {niveles[prediccion]}')
print("<----- Jugador Cuatro ----->")
nuevo_jugador_cuatro = np.array([[1, 1, 1, 0]])
prediccion = modelo.predict(nuevo_jugador_cuatro)[0]
print(f'El nuevo jugador es: {niveles[prediccion]}')



