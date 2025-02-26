# Heuristica simple para encontrar el numero mas cercano al objetivo
def heuristica(a, b):
    return abs(a - b)

#Resolver un problema simple 
objetivo = 50
valores = [20, 35, 55, 60, 70]

# Encontrar el valor mas cercano al objetivo usando heuristica
mejor_valor = min(valores, key=lambda x: heuristica(x, objetivo))
print(f"El valor mas cercano al objetivo {objetivo} es {mejor_valor}")