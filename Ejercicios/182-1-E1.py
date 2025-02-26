# Implementacion simple del algoritomo A* (esto requiere una heuristica)
import heapq

def a_estrella(grafo, inicio, fin, heuristica):
    abierta = []
    cerrada = set()
    heapq.heappush(abierta, (0 + heuristica(inicio), 0, inicio,[]))

    while abierta:
        _, costo, nodo, camino = heapq.heappop(abierta)
        if nodo in cerrada:
            continue
        camino = camino + [nodo]
        if nodo == fin:
            return camino
        cerrada.add(nodo)
        for vecino, peso in grafo.get(nodo,[]):
            if vecino not in cerrada:
                heapq.heappush(abierta, (costo * peso + heuristica(vecino), costo * peso, vecino, camino))
    return None