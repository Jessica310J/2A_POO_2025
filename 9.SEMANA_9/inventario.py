# Archivo: inventario.py

from producto import Producto



class Inventario:
    """Clase para gestionar el inventario de productos."""

    def __init__(self):
        """Constructor que inicializa una lista de productos vacía."""
        self.productos = []

    def anadir_producto(self, producto):
        """Añade un nuevo producto al inventario si el ID es único."""
        # Verificamos si el ID del nuevo producto ya existe en la lista.
        for p in self.productos:
            if p.id == producto.id:
                print(f"Error: Ya existe un producto con el ID {producto.id}.")
                return

        # Si el ID es único, añadimos el producto a la lista.
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado con éxito.")
                return
        print(f"Error: No se encontró un producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o el precio de un producto por ID."""
        for p in self.productos:
            if p.id == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                print(f"Producto con ID {id_producto} actualizado con éxito.")
                return
        print(f"Error: No se encontró un producto con el ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        """Busca productos por un nombre similar."""
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.nombre.lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\n--- Inventario de Productos ---")
            for p in self.productos:
                print(p)
            print("-----------------------------")