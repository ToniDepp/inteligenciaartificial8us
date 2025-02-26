# Implementacion de DFS (Depth_First Search)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return visitados

# Ejemplo de uso
resultado = dfs(grafo, 'A')
print(f"Nodos visitados por DFS: {resultado}")