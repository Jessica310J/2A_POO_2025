
# Este programa define una clase Tablet que utiliza constructores y destructores.
# La clase permite crear objetos que representan tablets, inicializando sus atributos
# y mostrando mensajes al crear y destruir los objetos.

class Tablet:
    def __init__(self, marca, sistema_operativo):
        self.marca = marca              # Inicializa los atributos de la tablet
        self.sistema_operativo = sistema_operativo
        print(f"Tablet {self.marca} con {self.sistema_operativo} inicializada")

    def __del__(self):
        print(f"Tablet {self.marca} siendo apagada")  # Mensaje al destruir el objeto

if __name__ == "__main__":
    mi_tablet = Tablet("Samsung", "Android 12") # Crear una instancia de Tablet
    print(f"Usando tablet {mi_tablet.marca}")
    del mi_tablet        # Llamada explícita al destructor

# Este código demuestra el uso de constructores para inicializar objetos y destructores
# para realizar limpieza al finalizar el uso de los objetos.


