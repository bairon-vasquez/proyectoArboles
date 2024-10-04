# controllers/main_controller.py
from PyQt5.QtWidgets import QMessageBox
from Backend.Services.ArbolAVL import ArbolAVL
from Backend.Models.Producto import Producto

class MainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.arbol = ArbolAVL()

    # Función para agregar un producto al árbol
    def agregar_producto(self):
        id_producto = self.main_window.input_id.text()
        nombre = self.main_window.input_nombre.text()
        cantidad = self.main_window.input_cantidad.text()
        precio = self.main_window.input_precio.text()
        categoria = self.main_window.input_categoria.text()

        # Verificar si los campos están completos
        if not id_producto or not nombre or not cantidad or not precio or not categoria:
            self._mostrar_error("Por favor, completa todos los campos")
            return
        
        # Crear producto e insertarlo en el árbol
        producto = Producto(int(id_producto), nombre, int(cantidad), float(precio), categoria)
        self.arbol.insertar(producto)
        
        # Limpiar campos de texto
        self.main_window.input_id.clear()
        self.main_window.input_nombre.clear()
        self.main_window.input_cantidad.clear()
        self.main_window.input_precio.clear()
        self.main_window.input_categoria.clear()

        # Actualizar la visualización del árbol
        self.mostrar_arbol()

    # Función para mostrar el árbol en el cuadro de visualización
    def mostrar_arbol(self):
        texto_arbol = self.arbol.mostrar_arbol()
        self.main_window.actualizar_visualizacion_arbol(texto_arbol)

    # Función para mostrar mensajes de error
    def _mostrar_error(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText(mensaje)
        msg.exec_()
