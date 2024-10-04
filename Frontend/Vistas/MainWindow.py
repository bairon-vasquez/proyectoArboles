# views/main_window.py

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from Controladores.MainController import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventario de Productos - Árbol AVL")
        self.setGeometry(100, 100, 800, 600)
        
        # Controlador principal que conecta con el backend
        self.controller = MainController(self)
        
        # Widget principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Cuadro de visualización del árbol
        self.tree_view = QLabel("Visualización del árbol AVL")
        self.layout.addWidget(self.tree_view)

        # Sección para agregar un producto
        self._crear_seccion_agregar_producto()

        # Botón para mostrar el árbol
        self.mostrar_arbol_button = QPushButton("Mostrar Árbol")
        self.mostrar_arbol_button.clicked.connect(self.controller.mostrar_arbol)
        self.layout.addWidget(self.mostrar_arbol_button)

    def _crear_seccion_agregar_producto(self):
        # Layout horizontal para los campos de texto
        layout_agregar = QHBoxLayout()

        # Campos de texto para ingresar datos del producto
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID del Producto")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre del Producto")
        self.input_cantidad = QLineEdit()
        self.input_cantidad.setPlaceholderText("Cantidad")
        self.input_precio = QLineEdit()
        self.input_precio.setPlaceholderText("Precio")
        self.input_categoria = QLineEdit()
        self.input_categoria.setPlaceholderText("Categoría")

        # Botón para agregar producto
        self.agregar_button = QPushButton("Agregar Producto")
        self.agregar_button.clicked.connect(self.controller.agregar_producto)

        # Agregar widgets al layout
        layout_agregar.addWidget(self.input_id)
        layout_agregar.addWidget(self.input_nombre)
        layout_agregar.addWidget(self.input_cantidad)
        layout_agregar.addWidget(self.input_precio)
        layout_agregar.addWidget(self.input_categoria)
        layout_agregar.addWidget(self.agregar_button)

        # Agregar el layout al layout principal
        self.layout.addLayout(layout_agregar)

    # Función para actualizar la visualización del árbol
    def actualizar_visualizacion_arbol(self, texto_arbol):
        self.tree_view.setText(texto_arbol)
