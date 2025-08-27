from producto import Producto

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar los productos.
        """
        self._productos = {}

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        """
        if producto.id in self._productos:
            print("❌ Error: Ya existe un producto con este ID.")
            return False
        self._productos[producto.id] = producto
        print(f"✅ Producto '{producto.nombre}' agregado correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        if id_producto in self._productos:
            del self._productos[id_producto]
            print(f"✅ Producto con ID {id_producto} eliminado.")
            return True
        print(f"❌ Error: No se encontró ningún producto con el ID {id_producto}.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto.
        """
        if id_producto in self._productos:
            producto = self._productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print(f"✅ Producto con ID {id_producto} actualizado.")
            return True
        print(f"❌ Error: No se encontró ningún producto con el ID {id_producto}.")
        return False

    def buscar_producto_por_nombre(self, nombre_busqueda):
        """
        Busca productos que contengan el nombre especificado.
        Utiliza una lista de comprensión para un código conciso.
        """
        resultados = [
            p for p in self._productos.values()
            if nombre_busqueda.lower() in p.nombre.lower()
        ]
        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self._productos:
            print("🛒 El inventario está vacío.")
            return

        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self._productos.values():
            print(producto)
        print("-------------------------\n")

    def get_productos_para_guardar(self):
        """
        Prepara los datos del inventario en un formato de diccionario
        para ser guardado.
        """
        return {id_prod: prod.to_dict() for id_prod, prod in self._productos.items()}

    def cargar_productos_desde_json(self, datos_json):
        """
        Carga productos desde un diccionario JSON.
        """
        self._productos.clear()
        for id_prod, datos_prod in datos_json.items():
            producto = Producto(
                datos_prod['id'],
                datos_prod['nombre'],
                datos_prod['cantidad'],
                datos_prod['precio']
            )
            self._productos[id_prod] = producto