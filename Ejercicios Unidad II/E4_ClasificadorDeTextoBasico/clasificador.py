from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Datos de ejemplo ampliados para mejorar la precisión
documents = [
    "El cielo es azul y brillante",
    "Me encanta ver las estrellas en el cielo nocturno",
    "Hoy el clima está soleado y hace calor",
    "Las nubes grises anuncian lluvia",
    "El perro es un gran compañero fiel",
    "Los gatos son animales muy independientes",
    "Los animales domésticos pueden ser cariñosos",
    "Me gusta jugar al fútbol los fines de semana",
    "El baloncesto es un deporte muy dinámico",
    "El tenis se juega en una cancha con una red",
    "El ciclismo es un deporte de resistencia",
    "Los deportes al aire libre son muy saludables"
]
labels = [
    "clima", "clima", "clima", "clima",
    "animales", "animales", "animales",
    "deportes", "deportes", "deportes", "deportes", "deportes"
]

# División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42, stratify=labels)

# Creación del modelo con un pipeline usando Logistic Regression
model = make_pipeline(TfidfVectorizer(ngram_range=(1,2)), LogisticRegression(max_iter=300, solver='lbfgs'))

# Entrenamiento del modelo
model.fit(X_train, y_train)

# Evaluación del modelo
accuracy = model.score(X_test, y_test)
print(f"Precisión del modelo: {accuracy:.2f}")

# Clasificar un nuevo texto
new_text = ["Hoy el clima está soleado y hace calor"]
prediction = model.predict(new_text)
print(f"El texto '{new_text[0]}' se clasifica como: {prediction[0]}")

new_text_one = ["Los gatos son animales muy independientes"]
prediction = model.predict(new_text_one)
print(f"El texto '{new_text_one[0]}' se clasifica como: {prediction[0]}")

new_text_two = ["El ciclismo es un deporte de resistencia"]
prediction = model.predict(new_text_two)
print(f"El texto '{new_text_two[0]}' se clasifica como: {prediction[0]}")