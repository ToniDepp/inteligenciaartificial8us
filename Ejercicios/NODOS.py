class Nodo:
    def _init_(self, dato):
        self.dato = dato  
        self.siguiente = None  

nodo1 = Nodo(5)

print("Valor del nodo:",nodo1.dato)