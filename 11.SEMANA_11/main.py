import json
import os
from inventario import Inventario
from producto import Producto

ARCHIVO_INVENTARIO = "inventario.json"

def guardar_inventario(inventario):
    """
    Guarda el inventario en un archivo JSON.
    """
    try:
        with open(ARCHIVO_INVENTARIO, "w") as f:
            json.dump(inventario.get_productos_para_guardar(), f, indent=4)
        print("✅ Inventario guardado con éxito.")
    except Exception as e:
        print(f"❌ Error al guardar el inventario: {e}")

def cargar_inventario():
    """
    Carga el inventario desde un archivo JSON.
    """
    inventario = Inventario()
    if os.path.exists(ARCHIVO_INVENTARIO):
        try:
            with open(ARCHIVO_INVENTARIO, "r") as f:
                datos = json.load(f)
                inventario.cargar_productos_desde_json(datos)
            print("✅ Inventario cargado desde el archivo.")
        except json.JSONDecodeError:
            print("⚠️ Archivo de inventario corrupto o vacío. Se iniciará uno nuevo.")
        except Exception as e:
            print(f"❌ Error al cargar el inventario: {e}")
    else:
        print("📦 No se encontró el archivo de inventario. Iniciando con un inventario vacío.")
    return inventario

def main():
    """
    Función principal del programa.
    """
    inventario = cargar_inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todo el inventario")
        print("6. Guardar y salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            try:
                id_prod = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("❌ Error: La cantidad y el precio deben ser números.")

        elif opcion == "2":
            id_prod = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("ID del producto a actualizar: ")

            nueva_cantidad_str = input("Nueva cantidad (presiona Enter para no cambiar): ")
            nuevo_precio_str = input("Nuevo precio (presiona Enter para no cambiar): ")

            nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None

            inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre_busqueda = input("Ingresa el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre_busqueda)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for producto in resultados:
                    print(producto)
            else:
                print("🔎 No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            guardar_inventario(inventario)
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()