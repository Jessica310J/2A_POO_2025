class TanqueCombustible:
    def __init__(self, capacidad):
        # Capacidad máxima del tanque (litros)
        self.__capacidad = capacidad
        # Cantidad actual de combustible (litros), privado
        self.__nivel = 0

    def llenar(self, litros):
        # Solo permite llenar si no excede la capacidad
        if litros + self.__nivel <= self.__capacidad:
            self.__nivel += litros
            print(f"Tanque llenado a {self.__nivel} litros.")
        else:
            print("Error: Excede la capacidad del tanque.")

    def consultar_nivel(self):
        # Permite consultar el nivel actual de combustible
        return self.__nivel

# Uso
tanque = TanqueCombustible(50)
tanque.llenar(20)          # Tanque llenado a 20 litros.
print(tanque.consultar_nivel())  # 20
tanque.llenar(40)          # Error: Excede la capacidad del tanque.
# print(tanque.__nivel)    # Error: atributo privado, no accesible directamente
