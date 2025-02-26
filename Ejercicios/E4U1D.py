# Simulacion de un agente cognocitivo tomando decisiones basadas en criterios predefinidos
opciones = ["Ir al cine","Estudiar","Hacer ejercicios"];

# Funcion para tomar una desicion basada en prioridades
def tomar_desicion(prioridades):
    for opcion in opciones:
        if opcion in prioridades:
            return f"El agente decide {opcion}"
    return "El agente no decide nada."

# Ejemplo de uso con diferentes prioridades
prioridades = ["Hacer ejercicio", "Estudiar"]
print(tomar_desicion(prioridades))