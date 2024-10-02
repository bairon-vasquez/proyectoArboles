# models/avl_node.py
class AVLNode:
    def __init__(self, product):
        self.product = product  # Instancia de Product
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
        self.height = 1  # Altura del nodo
