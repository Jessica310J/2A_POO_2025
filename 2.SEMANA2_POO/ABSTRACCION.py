class Vehiculo:
    def __init__(self, marca, modelo):
        # Guardamos la marca y modelo del vehículo
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        # Método abstracto: se espera que cada tipo de vehículo implemente cómo arranca
        raise NotImplementedError("Este método debe implementarse en la subclase")


class Auto(Vehiculo):
    def arrancar(self):
        # Implementación específica para un auto
        print(f"El auto {self.marca} {self.modelo} ha arrancado.")


class Moto(Vehiculo):
    def arrancar(self):
        # Implementación específica para una moto
        print(f"La moto {self.marca} {self.modelo} ha arrancado.")


# Uso
auto = Auto("Toyota", "Corolla")
moto = Moto("Honda", "CBR")

auto.arrancar()
moto.arrancar()
