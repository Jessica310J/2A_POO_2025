import os  # Importamos el módulo para interactuar con el sistema de archivos
from producto import Producto


class Inventario:
    """Clase para gestionar el inventario de productos con persistencia en archivos."""

    def __init__(self, archivo_inventario='inventario.txt'):
        """
        Constructor que inicializa el inventario y carga los datos desde un archivo.
        """
        self.productos = {}  # ¡Cambiado de una lista a un diccionario para un acceso rápido!
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()  # Llama al método para cargar los datos al iniciar

    def _guardar_inventario(self):
        """
        Guarda el estado actual del inventario en un archivo de texto.
        Maneja excepciones para errores de E/S (Escritura/Lectura).
        """
        try:
            # Usamos 'w' para sobrescribir el archivo y asegurar que los datos estén sincronizados
            with open(self.archivo_inventario, 'w') as f:
                for producto in self.productos.values():
                    # Escribe cada producto en una nueva línea con un formato simple (id,nombre,cantidad,precio)
                    f.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("✅ Inventario guardado exitosamente.")
        except IOError as e:
            print(f"❌ Error al guardar el inventario: {e}")
            print("Verifique los permisos de escritura del archivo.")

    def cargar_inventario(self):
        """
        Carga el inventario desde un archivo de texto. Maneja la ausencia del archivo
        y errores de lectura/formato de datos.
        """
        # Verifica si el archivo existe. Si no, no hace nada y se creará al guardar.
        if not os.path.exists(self.archivo_inventario):
            print("ℹ️ El archivo de inventario no existe. Se creará uno nuevo al guardar.")
            return

        try:
            # 'r' es el modo de lectura (read)
            with open(self.archivo_inventario, 'r') as f:
                for linea in f:
                    try:
                        # Limpia espacios y divide la línea por comas
                        partes = linea.strip().split(',')
                        if len(partes) == 4:
                            id_prod, nombre, cantidad, precio = partes
                            # Convierte a los tipos de datos correctos
                            self.productos[id_prod] = Producto(id_prod, nombre, int(cantidad), float(precio))
                    except (ValueError, IndexError) as e:
                        # Este bloque captura si una línea del archivo está mal formada
                        print(f"⚠️ Línea con formato incorrecto en el archivo: '{linea.strip()}' - Error: {e}")
            print("✅ Inventario cargado exitosamente.")
        except PermissionError:
            print(f"❌ Error de permisos: No se puede leer el archivo '{self.archivo_inventario}'.")
        except IOError as e:
            print(f"❌ Error de E/S al leer el archivo: {e}")

    def anadir_producto(self, producto):
        """Añade un nuevo producto y guarda el cambio."""
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.id}.")
            return False

        self.productos[producto.id] = producto
        self._guardar_inventario()  # Llama a guardar después de un cambio exitoso
        print(f"✅ Producto '{producto.nombre}' añadido con éxito.")
        return True

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID y guarda el cambio."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self._guardar_inventario()  # Llama a guardar después de un cambio exitoso
            print(f"✅ Producto con ID {id_producto} eliminado con éxito.")
            return True
        else:
            print(f"Error: No se encontró un producto con el ID {id_producto}.")
            return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o el precio de un producto y guarda el cambio."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio

            self._guardar_inventario()  # Llama a guardar después de un cambio exitoso
            print(f"✅ Producto con ID {id_producto} actualizado con éxito.")
            return True
        else:
            print(f"Error: No se encontró un producto con el ID {id_producto}.")
            return False

    def buscar_producto_por_nombre(self, nombre):
        """Busca productos por un nombre similar."""
        resultados = []
        # Ahora recorre los valores del diccionario
        for p in self.productos.values():
            if nombre.lower() in p.nombre.lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\n--- Inventario de Productos ---")
            # Ahora recorre los valores del diccionario
            for p in self.productos.values():
                print(p)
            print("-----------------------------")