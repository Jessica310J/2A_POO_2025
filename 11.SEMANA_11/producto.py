class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa un nuevo producto con sus atributos.
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id(self):
        """Getter para obtener el ID del producto."""
        return self._id

    @property
    def nombre(self):
        """Getter y setter para el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def cantidad(self):
        """Getter y setter para la cantidad del producto."""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @property
    def precio(self):
        """Getter y setter para el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def to_dict(self):
        """
        Convierte el objeto Producto a un diccionario para serializarlo en JSON.
        """
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Producto.
        """
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"