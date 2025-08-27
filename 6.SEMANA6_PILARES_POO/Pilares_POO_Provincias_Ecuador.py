# -----------------------------------------------
# PROGRAMA: PROVINCIAS DEL ECUADOR (POO EN PYTHON)
# Autor: [Jessica Pesantez]
# Fecha: [04-07-2025]
# -----------------------------------------------

###  CLASE BASE (Provincia) ###
class Provincia:
    def __init__(self, nombre, capital):
        self.nombre = nombre  # Atributo público
        self.capital = capital  # Atributo público
        self.__poblacion = 0  # Atributo privado (encapsulado)

    # Método polimórfico (se sobrescribirá)
    def mostrar_info(self):
        pass

    # Getter (encapsulación)
    def obtener_poblacion(self):
        return self.__poblacion

    # Setter (encapsulación)
    def _establecer_poblacion(self, poblacion):
        if poblacion > 0:
            self.__poblacion = poblacion
        else:
            print("Error: Población debe ser positiva")


###  CLASE DERIVADA (ProvinciaConRegion) ###
class ProvinciaConRegion(Provincia):
    def __init__(self, nombre, capital, region, dato_curioso):
        super().__init__(nombre, capital)  # Hereda de Provincia
        self.region = region  # Atributo extra
        self.dato_curioso = dato_curioso  # Atributo extra

    # Sobreescribe el método (Polimorfismo)
    def mostrar_info(self):
        return (f" {self.nombre}\n"
                f"   Capital: {self.capital}\n"
                f"   Región: {self.region}\n"
                f"   Población: {self.obtener_poblacion():,} habitantes\n"
                f"   Dato curioso: {self.dato_curioso}\n")


### DATOS DE PROVINCIAS (EJEMPLO) ###
def cargar_provincias():
    provincias = [
        ProvinciaConRegion("Azuay", "Cuenca", "Sierra",
                           "Tiene el Centro Histórico más grande del país."),
        ProvinciaConRegion("Pichincha", "Quito", "Sierra",
                           "Capital del Ecuador y Patrimonio Cultural de la Humanidad."),
        ProvinciaConRegion("Guayas", "Guayaquil", "Costa",
                           "Puerto principal del país con clima tropical."),
        ProvinciaConRegion("El Oro", "Machala", "Costa",
                           "Llamada 'Capital Bananera del Mundo'."),
        ProvinciaConRegion("Galápagos", "Puerto Baquerizo Moreno", "Insular",
                           "Patrimonio Natural de la Humanidad por su biodiversidad única.")
    ]

    # Establecemos poblaciones (datos aproximados 2023)
    provincias[0]._establecer_poblacion(800000)  # Azuay
    provincias[1]._establecer_poblacion(3000000)  # Pichincha
    provincias[2]._establecer_poblacion(4500000)  # Guayas
    provincias[3]._establecer_poblacion(700000)  # El Oro
    provincias[4]._establecer_poblacion(30001)  # Galápagos

    return provincias


###  DEMOSTRACIÓN ###
if __name__ == "__main__":
    # Cargamos las provincias
    lista_provincias = cargar_provincias()

    # Mostramos información
    print("\n PROVINCIAS DEL ECUADOR (POO) \n")
    for provincia in lista_provincias:
        print(provincia.mostrar_info())

    print(" Programa ejecutado correctamente")
