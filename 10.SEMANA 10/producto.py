# Archivo: producto.py

class Producto:
    """Clase para representar un producto en el inventario."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor para inicializar un objeto Producto."""
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Retorna una representación en string del objeto Producto."""
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"