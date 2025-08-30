from inventario import Inventario
from producto import Producto


def main():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_prod = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo_prod = Producto(id_prod, nombre, cantidad, precio)
                inventario.anadir_producto(nuevo_prod)
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")

        elif opcion == '2':
            id_prod = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("ID del producto a actualizar: ")
            nueva_cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")

            nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None

            inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()