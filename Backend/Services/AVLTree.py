# services/avl_tree.py
from Backend.Models.AVLNode import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None

    # Función para obtener la altura de un nodo
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Función para rotación a la derecha
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    # Función para rotación a la izquierda
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        return y

    # Obtener el factor de balance de un nodo
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Inserción en el árbol AVL
    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if not node:
            return AVLNode(product)

        if product.product_id < node.product.product_id:
            node.left = self._insert(node.left, product)
        else:
            node.right = self._insert(node.right, product)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Rotaciones para mantener balance
        if balance > 1 and product.product_id < node.left.product.product_id:
            return self._rotate_right(node)
        if balance < -1 and product.product_id > node.right.product.product_id:
            return self._rotate_left(node)
        if balance > 1 and product.product_id > node.left.product.product_id:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and product.product_id < node.right.product.product_id:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Búsqueda de un producto por ID
    def search(self, product_id):
        return self._search(self.root, product_id)

    def _search(self, node, product_id):
        if not node or node.product.product_id == product_id:
            return node
        if product_id < node.product.product_id:
            return self._search(node.left, product_id)
        return self._search(node.right, product_id)

    # Eliminar un nodo en el árbol AVL
    def delete(self, product_id):
        self.root = self._delete(self.root, product_id)

    def _delete(self, node, product_id):
        # Implementar lógica de eliminación similar a la inserción
        pass

    # Visualización del árbol (simplificada)
    def display_tree(self):
        lines = []
        self._display_tree(self.root, 0, lines)
        return "\n".join(lines)

    def _display_tree(self, node, level, lines):
        if node:
            self._display_tree(node.right, level + 1, lines)
            lines.append(' ' * 4 * level + f'-> {node.product.product_id}')
            self._display_tree(node.left, level + 1, lines)
