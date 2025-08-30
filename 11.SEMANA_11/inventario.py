import os
from producto import Producto

class Inventario:
    """Clase para gestionar el inventario de productos."""

    def __init__(self, archivo_inventario='inventario.txt'):
        self.productos = {}
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def guardar_inventario(self):
        """Guarda el inventario en un archivo de texto."""
        with open(self.archivo_inventario, 'w') as f:
            for p in self.productos.values():
                f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto."""
        if not os.path.exists(self.archivo_inventario):
            return
        with open(self.archivo_inventario, 'r') as f:
            for linea in f:
                partes = linea.strip().split(',')
                if len(partes) == 4:
                    id_prod, nombre, cantidad, precio = partes
                    self.productos[id_prod] = Producto(id_prod, nombre, int(cantidad), float(precio))

    def anadir_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.id}.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        else:
            print(f"Error: No se encontró un producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado con éxito.")
        else:
            print(f"Error: No se encontró un producto con el ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for p in self.productos.values():
            if nombre.lower() in p.nombre.lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\n--- Inventario de Productos ---")
            for p in self.productos.values():
                print(p)
            print("-----------------------------")