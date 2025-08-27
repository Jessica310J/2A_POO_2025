class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        print(f"Vehículo de marca {self.marca}")

class Barco(Vehiculo):
    def describir(self):
        # Sobrescribimos el método para describir un barco
        print(f"Barco de marca {self.marca} navegando en el agua.")

class Avion(Vehiculo):
    def describir(self):
        # Sobrescribimos el método para describir un avión
        print(f"Avión de marca {self.marca} volando en el cielo.")

# Uso
vehiculos = [Barco("Yamaha"), Avion("Boeing")]
for v in vehiculos:
    v.describir()
