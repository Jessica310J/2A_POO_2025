# usuario.py

class Usuario:
    """
    Usuario con nombre, ID único y lista de libros prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return True
        return False

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"