# models/product.py
class Product:
    def __init__(self, product_id, name, quantity, price, category):
        self.product_id = product_id  # ID del producto, clave en el AVL
        self.name = name  # Nombre del producto
        self.quantity = quantity  # Cantidad disponible
        self.price = price  # Precio del producto
        self.category = category  # Categoría del producto
