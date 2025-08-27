class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        print(f"Ingreso: Vehículo con placa {self.placa}")

    def __del__(self):
        print(f"Salida: Vehículo con placa {self.placa}")

class Parqueadero:
    def __init__(self):
        self.vehiculos = []  # Lista para almacenar vehículos

    def ingresar_vehiculo(self, placa):
        if len(self.vehiculos) < 2:  # Limitar a dos vehículos
            nuevo_vehiculo = Vehiculo(placa)
            self.vehiculos.append(nuevo_vehiculo)
        else:
            print("Parqueadero lleno.")

    def salir_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                self.vehiculos.remove(vehiculo)
                del vehiculo  # Destructor se llama automáticamente
                return
        print("Vehículo no encontrado.")

# Ejecución
parqueadero = Parqueadero()
parqueadero.ingresar_vehiculo("ABC-123")  # Placa de la ciudad de Quito
parqueadero.ingresar_vehiculo("XYZ-456")  # Placa  de la ciudad de Quito
parqueadero.ingresar_vehiculo("LMN-789")  # Intento de ingreso adicional
parqueadero.salir_vehiculo("ABC-123")  # Salida del primer vehículo


