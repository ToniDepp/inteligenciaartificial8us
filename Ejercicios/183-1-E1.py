# Implementacion simple de descenso de colina
def funcion_obejetivo(x):
    return x**2 - 4*x + 4

def descenso_colina(inicio, tasa_aprendizaje=0.1, iteraciones=100):
    x = inicio
    for _ in range(iteraciones):
        gradiente = 2*x - 4 # Derivada de la funcion
        x = x - tasa_aprendizaje * gradiente # Actualizacion 
    return x

# Ejemplo de uso
solucion = descenso_colina(0)
print(f"La solucion optima es: {solucion}")

