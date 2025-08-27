class Vehiculo:
    def moverse(self):
        # Método base, se redefine en cada tipo de vehículo
        pass

class Bicicleta(Vehiculo):
    def moverse(self):
        print("La bicicleta pedalea por la carretera.")

class Carro(Vehiculo):
    def moverse(self):
        print("El carro conduce por la autopista.")

class Helicoptero(Vehiculo):
    def moverse(self):
        print("El helicóptero vuela sobre la ciudad.")

# Uso
flota = [Bicicleta(), Carro(), Helicoptero()]
for vehiculo in flota:
    vehiculo.moverse()
