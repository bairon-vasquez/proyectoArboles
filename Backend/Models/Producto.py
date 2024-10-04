# models/producto.py
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio, categoria):
        self.id_producto = id_producto  # ID del producto, clave en el AVL
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio del producto
        self.categoria = categoria  # Categoría del producto
