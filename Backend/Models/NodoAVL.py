# models/nodo_avl.py
class NodoAVL:
    def __init__(self, producto):
        self.producto = producto  # Instancia de Producto
        self.izquierda = None  # Hijo izquierdo
        self.derecha = None  # Hijo derecho
        self.altura = 1  # Altura del nodo
