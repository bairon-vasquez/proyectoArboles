# services/avl_tree.py
from Backend.Models.NodoAVL import NodoAVL
from Backend.Models.Producto import Producto
import json

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    # Función para obtener la altura de un nodo
    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Función para rotación a la derecha
    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha)) + 1
        x.altura = max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha)) + 1
        return x

    # Función para rotación a la izquierda
    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha)) + 1
        y.altura = max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha)) + 1
        return y

    # Obtener el factor de balance de un nodo
    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    # Inserción en el árbol AVL
    def insertar(self, producto):
        self.raiz = self._insertar(self.raiz, producto)

    def _insertar(self, nodo, producto):
        if not nodo:
            return NodoAVL(producto)

        if producto.id_producto < nodo.producto.id_producto:
            nodo.izquierda = self._insertar(nodo.izquierda, producto)
        else:
            nodo.derecha = self._insertar(nodo.derecha, producto)

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))
        balance = self._obtener_balance(nodo)

        # Rotaciones para mantener balance
        if balance > 1 and producto.id_producto < nodo.izquierda.producto.id_producto:
            return self._rotar_derecha(nodo)
        if balance < -1 and producto.id_producto > nodo.derecha.producto.id_producto:
            return self._rotar_izquierda(nodo)
        if balance > 1 and producto.id_producto > nodo.izquierda.producto.id_producto:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and producto.id_producto < nodo.derecha.producto.id_producto:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    # Búsqueda de un producto por ID
    def buscar(self, id_producto):
        return self._buscar(self.raiz, id_producto)

    def _buscar(self, nodo, id_producto):
        if not nodo or nodo.producto.id_producto == id_producto:
            return nodo
        if id_producto < nodo.producto.id_producto:
            return self._buscar(nodo.izquierda, id_producto)
        return self._buscar(nodo.derecha, id_producto)

    # Eliminar un nodo en el árbol AVL
    def eliminar(self, id_producto):
        self.raiz = self._eliminar(self.raiz, id_producto)

    def _eliminar(self, nodo, id_producto):
        # Implementar lógica de eliminación similar a la inserción
        pass

    # Visualización del árbol (simplificada)
    def mostrar_arbol(self):
        lineas = []
        self._mostrar_arbol(self.raiz, 0, lineas)
        return "\n".join(lineas)

    def _mostrar_arbol(self, nodo, nivel, lineas):
        if nodo:
            self._mostrar_arbol(nodo.derecha, nivel + 1, lineas)
            lineas.append(' ' * 4 * nivel + f'-> {nodo.producto.id_producto}')
            self._mostrar_arbol(nodo.izquierda, nivel + 1, lineas)



    # Eliminar un nodo en el árbol AVL
    def _eliminar(self, nodo, id_producto):
        # Paso 1: Realizar la eliminación estándar de BST
        if not nodo:
            return nodo

        if id_producto < nodo.producto.id_producto:
            nodo.izquierda = self._eliminar(nodo.izquierda, id_producto)
        elif id_producto > nodo.producto.id_producto:
            nodo.derecha = self._eliminar(nodo.derecha, id_producto)
        else:
            # Nodo con solo un hijo o sin hijos
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp

            # Nodo con dos hijos: obtener el sucesor (el menor en el subárbol derecho)
            temp = self._obtener_menor(nodo.derecha)
            nodo.producto = temp.producto
            nodo.derecha = self._eliminar(nodo.derecha, temp.producto.id_producto)

        # Si el árbol tiene un solo nodo
        if nodo is None:
            return nodo

        # Paso 2: Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

        # Paso 3: Obtener el factor de balance y balancear el nodo
        balance = self._obtener_balance(nodo)

        # Si el nodo está desbalanceado, hay 4 casos posibles

        # Caso Izquierda-Izquierda
        if balance > 1 and self._obtener_balance(nodo.izquierda) >= 0:
            return self._rotar_derecha(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and self._obtener_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and self._obtener_balance(nodo.derecha) <= 0:
            return self._rotar_izquierda(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and self._obtener_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    # Función para obtener el nodo con el valor menor (usado en la eliminación)
    def _obtener_menor(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual


# services/arbol_avl.py

    # Guardar el árbol AVL en un archivo JSON
    def guardar_arbol(self, nombre_archivo):
        datos_arbol = self._serializar_arbol(self.raiz)
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_arbol, archivo, indent=4)

    # Serializar el árbol a un diccionario
    def _serializar_arbol(self, nodo):
        if nodo is None:
            return None
        return {
            'producto': {
                'id_producto': nodo.producto.id_producto,
                'nombre': nodo.producto.nombre,
                'cantidad': nodo.producto.cantidad,
                'precio': nodo.producto.precio,
                'categoria': nodo.producto.categoria
            },
            'izquierda': self._serializar_arbol(nodo.izquierda),
            'derecha': self._serializar_arbol(nodo.derecha),
            'altura': nodo.altura
        }

# services/arbol_avl.py

    # Cargar el árbol AVL desde un archivo JSON
    def cargar_arbol(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            datos_arbol = json.load(archivo)
            self.raiz = self._deserializar_arbol(datos_arbol)

    # Deserializar el diccionario a un árbol AVL
    def _deserializar_arbol(self, datos):
        if datos is None:
            return None
        producto = Producto(
            datos['producto']['id_producto'],
            datos['producto']['nombre'],
            datos['producto']['cantidad'],
            datos['producto']['precio'],
            datos['producto']['categoria']
        )
        nodo = NodoAVL(producto)
        nodo.izquierda = self._deserializar_arbol(datos['izquierda'])
        nodo.derecha = self._deserializar_arbol(datos['derecha'])
        nodo.altura = datos['altura']
        return nodo

# services/arbol_avl.py

    # Buscar productos dentro de un rango de precios
    def buscar_por_precio(self, precio_min, precio_max):
        productos_en_rango = []
        self._buscar_por_precio(self.raiz, precio_min, precio_max, productos_en_rango)
        return productos_en_rango

    def _buscar_por_precio(self, nodo, precio_min, precio_max, productos_en_rango):
        if not nodo:
            return
        if precio_min <= nodo.producto.precio <= precio_max:
            productos_en_rango.append(nodo.producto)
        if nodo.izquierda:
            self._buscar_por_precio(nodo.izquierda, precio_min, precio_max, productos_en_rango)
        if nodo.derecha:
            self._buscar_por_precio(nodo.derecha, precio_min, precio_max, productos_en_rango)

# services/arbol_avl.py

    # Buscar productos por categoría
    def buscar_por_categoria(self, categoria):
        productos_en_categoria = []
        self._buscar_por_categoria(self.raiz, categoria, productos_en_categoria)
        return productos_en_categoria

    def _buscar_por_categoria(self, nodo, categoria, productos_en_categoria):
        if not nodo:
            return
        if nodo.producto.categoria == categoria:
            productos_en_categoria.append(nodo.producto)
        if nodo.izquierda:
            self._buscar_por_categoria(nodo.izquierda, categoria, productos_en_categoria)
        if nodo.derecha:
            self._buscar_por_categoria(nodo.derecha, categoria, productos_en_categoria)
