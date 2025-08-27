# Definición de la clase ClimaSemanal
class ClimaSemanal:
    # Método constructor de la clase
    def __init__(self):
        # Inicializa una lista vacía para almacenar las temperaturas diarias
        self.temperaturas_diarias = []

    # Método para que el usuario ingrese las temperaturas
    def ingresar_temperaturas(self):
        print("Por favor, ingrese la temperatura para cada uno de los 7 días de la semana:")
        # Bucle para obtener las temperaturas de los 7 días
        for i in range(7):
            while True:  # Bucle para validar la entrada
                try:
                    # Solicita y convierte la temperatura a flotante
                    temp = float(input(f"Día {i + 1}: "))
                    # Añade la temperatura a la lista de la instancia
                    self.temperaturas_diarias.append(temp)
                    break  # Sale del bucle de validación
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        # Verifica si hay temperaturas para evitar división por cero
        if not self.temperaturas_diarias:
            return 0
        # Suma todas las temperaturas
        suma_temperaturas = sum(self.temperaturas_diarias)
        # Calcula el promedio
        promedio = suma_temperaturas / len(self.temperaturas_diarias)
        return promedio  # Retorna el promedio

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    # Crea una instancia de la clase ClimaSemanal
    mi_clima = ClimaSemanal()
    # Llama al método para ingresar las temperaturas
    mi_clima.ingresar_temperaturas()
    # Llama al método para calcular el promedio
    promedio_clima_oop = mi_clima.calcular_promedio()
    # Imprime el promedio semanal formateado
    print(f"\nEl promedio semanal del clima (POO) es: {promedio_clima_oop:.2f}°C")