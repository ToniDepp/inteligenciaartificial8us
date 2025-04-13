import networkx as nx  # Importamos la librería networkx para trabajar con grafos
import matplotlib.pyplot as plt  # Importamos matplotlib para la visualización del grafo

# Crear el grafo dirigido
g = nx.DiGraph()

# Agregar nodos
g.add_nodes_from(["Ecosistema", "Animal", "Planta", "Mamífero", "Ave", "Carnívoro", "Herbívoro", "León", "Cebra", "Árbol"])

# Agregar relaciones entre los nodos
g.add_edges_from([
    ("Ecosistema", "Animal"),
    ("Ecosistema", "Planta"),
    ("Animal", "Mamífero"),
    ("Animal", "Ave"),
    ("Mamífero", "Carnívoro"),
    ("Mamífero", "Herbívoro"),
    ("Carnívoro", "León"),
    ("Herbívoro", "Cebra"),
    ("Planta", "Árbol")
])

# Dibujar el grafo
plt.figure(figsize=(10, 6))
nx.draw(g, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
plt.show()