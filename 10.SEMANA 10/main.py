# Archivo: main.py

# Importamos las clases que vamos a usar.
from inventario import Inventario
from producto import Producto


def menu_principal():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")



def main():
    """Función principal del programa."""
    # La clase Inventario se encarga de cargar el archivo al iniciar
    inventario = Inventario()

    while True:
        opcion = menu_principal()

        if opcion == '1':
            try:
                id_producto = input("Ingrese el ID del producto: ")
                if not id_producto:
                    print("⚠️ El ID no puede estar vacío.")
                    continue
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.anadir_producto(nuevo_producto)
            except ValueError:
                print("❌ Error: Cantidad y precio deben ser números válidos.")

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")

            # Verificamos si el producto existe antes de solicitar más datos.
            if id_producto not in inventario.productos:
                print("⚠️ Error: Producto no encontrado.")
                continue

            print("Deje en blanco si no desea actualizar el campo.")
            nueva_cantidad_input = input(f"Ingrese la nueva cantidad ({inventario.productos[id_producto].cantidad}): ")
            nuevo_precio_input = input(f"Ingrese el nuevo precio ({inventario.productos[id_producto].precio}): ")

            try:
                # Si la entrada no está vacía, la convertimos a un número. De lo contrario, usamos None.
                nueva_cantidad = int(nueva_cantidad_input) if nueva_cantidad_input else None
                nuevo_precio = float(nuevo_precio_input) if nuevo_precio_input else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("❌ Error: Cantidad y precio deben ser números válidos.")

        elif opcion == '4':
            nombre_busqueda = input("Ingrese el nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre_busqueda)
            if resultados:
                print("\n--- Resultados de Búsqueda ---")
                for p in resultados:
                    print(p)
                print("-----------------------------")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()