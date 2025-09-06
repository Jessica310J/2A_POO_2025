# biblioteca.py

from libro import Libro
from usuario import Usuario

class Biblioteca:
    """
    Gestiona libros, usuarios y préstamos.
    """
    def __init__(self):
        self.libros = {}       # ISBN -> Libro
        self.usuarios = {}     # ID -> Usuario
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("Libro ya existe.")
            return False
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")
        return True

    def quitar_libro(self, isbn):
        if isbn not in self.libros:
            print("Libro no encontrado.")
            return False
        for u in self.usuarios.values():
            if any(l.isbn == isbn for l in u.libros_prestados):
                print("Libro está prestado, no se puede eliminar.")
                return False
        del self.libros[isbn]
        print(f"Libro con ISBN {isbn} eliminado.")
        return True

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("ID de usuario ya registrado.")
            return False
        self.usuarios[usuario.id_usuario] = usuario
        self.ids_usuarios.add(usuario.id_usuario)
        print(f"Usuario registrado: {usuario}")
        return True

    def dar_baja_usuario(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no encontrado.")
            return False
        if self.usuarios[id_usuario].libros_prestados:
            print("Usuario tiene libros prestados, no se puede dar de baja.")
            return False
        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario con ID {id_usuario} dado de baja.")
        return True

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return False
        if isbn not in self.libros:
            print("Libro no disponible.")
            return False
        for u in self.usuarios.values():
            if any(l.isbn == isbn for l in u.libros_prestados):
                print("Libro ya está prestado.")
                return False
        self.usuarios[id_usuario].prestar_libro(self.libros[isbn])
        print(f"Libro '{self.libros[isbn].titulo}' prestado a {self.usuarios[id_usuario].nombre}.")
        return True

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return False
        if self.usuarios[id_usuario].devolver_libro(isbn):
            print(f"Libro con ISBN {isbn} devuelto por {self.usuarios[id_usuario].nombre}.")
            return True
        print("El usuario no tiene ese libro prestado.")
        return False

    def buscar_por_titulo(self, titulo):
        return [l for l in self.libros.values() if titulo.lower() in l.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [l for l in self.libros.values() if autor.lower() in l.autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [l for l in self.libros.values() if categoria.lower() == l.categoria.lower()]

    def listar_libros_prestados_usuario(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return []
        return self.usuarios[id_usuario].libros_prestados