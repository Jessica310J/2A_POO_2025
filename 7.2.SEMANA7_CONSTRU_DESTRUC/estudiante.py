# Ejemplo de clase Estudiante con constructor y destructor
class Estudiante:
    def __init__(self, nombre, edad, carrera):     # Inicializa los atributos del estudiante
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante {self.nombre} de {self.edad} años en la carrera de {self.carrera} registrado.")

    def mostrar_informacion(self):

        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}") # Muestra la información del estudiante

    def __del__(self):       # El método __del__ es el DESTRUCTOR de la clase

        print(f"Estudiante {self.nombre} eliminado del sistema.")  # Mensaje al eliminar el estudiante



if __name__ == "__main__": # Ejemplo de uso
    estudiante1 = Estudiante("Carolina Montenegro", 30, "Ingeniera en Tecnologías de la Información")


    # 2. Uso del objeto
    estudiante1.mostrar_informacion()

    # 3. Destrucción del objeto
    del estudiante1

    #El ejemplo simula un sistema básico de gestión estudiantil
    #se registra, consulta y elimina información de estudiantes
