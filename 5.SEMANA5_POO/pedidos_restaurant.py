"""
Sistema de pedidos en un restaurante

Una persona puede hacer un pedido de comida de un menú disponible.
"""

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def hacer_pedido(self, restaurante, nombre_plato: str):
        print(f"\n{self.nombre} desea ordenar '{nombre_plato}'.")
        restaurante.procesar_pedido(self, nombre_plato)


class Plato:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class Restaurante:
    def __init__(self):
        self.menu = []

    def agregar_plato(self, plato: Plato):
        self.menu.append(plato)

    def mostrar_menu(self):
        print("\nMenú del restaurante:")
        for plato in self.menu:
            print(f"- {plato.nombre} - ${plato.precio:.2f}")

    def procesar_pedido(self, persona: Persona, nombre_plato: str):
        for plato in self.menu:
            if plato.nombre.lower() == nombre_plato.lower():
                print(f"{persona.nombre}, tu pedido de '{plato.nombre}' ha sido registrado. Total a pagar: ${plato.precio:.2f}")
                return
        print(f"Lo sentimos {persona.nombre}, el plato '{nombre_plato}' no está en el menú.")


def main():
    # Crear el restaurante y su menú
    restaurante = Restaurante()
    restaurante.agregar_plato(Plato("Hamburguesa", 5.50))
    restaurante.agregar_plato(Plato("Pizza", 7.25))
    restaurante.agregar_plato(Plato("Ensalada", 4.00))

    # Crear una persona
    nombre_usuario = input("Bienvenido al restaurante. ¿Cuál es tu nombre? ")
    persona = Persona(nombre_usuario)

    restaurante.mostrar_menu()

    plato_solicitado = input("\n¿Qué plato deseas ordenar? ")
    persona.hacer_pedido(restaurante, plato_solicitado)


if __name__ == "__main__":
    main()
