# Función para obtener las temperaturas diarias del usuario
def obtener_temperaturas_diarias():
    temperaturas = []  # Inicializa una lista vacía para almacenar las temperaturas
    print("Por favor, ingrese la temperatura para cada uno de los 7 días de la semana:")
    # Bucle para solicitar la temperatura de cada uno de los 7 días
    for i in range(7):
        while True:  # Bucle para asegurar una entrada válida
            try:
                # Solicita la temperatura para el día actual y la convierte a float
                temp = float(input(f"Día {i + 1}: "))
                temperaturas.append(temp)  # Agrega la temperatura a la lista
                break  # Sale del bucle si la entrada es válida
            except ValueError:
                # Maneja el error si la entrada no es un número
                print("Entrada inválida. Por favor, ingrese un número.")
    return temperaturas  # Retorna la lista de temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    if not temperaturas:  # Verifica si la lista de temperaturas está vacía
        return 0  # Si está vacía, retorna 0 para evitar división por cero
    suma_temperaturas = sum(temperaturas)  # Suma todas las temperaturas en la lista
    promedio = suma_temperaturas / len(temperaturas)  # Calcula el promedio
    return promedio  # Retorna el promedio

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    # Llama a la función para obtener las temperaturas diarias
    temps_semanales = obtener_temperaturas_diarias()
    # Llama a la función para calcular el promedio semanal con las temperaturas obtenidas
    promedio_clima = calcular_promedio_semanal(temps_semanales)
    # Imprime el resultado del promedio semanal formateado a dos decimales
    print(f"\nEl promedio semanal del clima es: {promedio_clima:.2f}°C")