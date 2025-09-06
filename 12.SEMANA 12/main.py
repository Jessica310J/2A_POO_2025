# main.py

from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "0987654321")
    libro3 = Libro("Python para Todos", "Raúl González", "Educativo", "1122334455")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios Jessica y Solange
    usuario1 = Usuario("Jessica", "U001")
    usuario2 = Usuario("Solange", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "1234567890")  # Jessica
    biblioteca.prestar_libro("U002", "0987654321")  # Solange

    # Listar libros prestados a Jessica
    print("\nLibros prestados a Jessica:")
    for libro in biblioteca.listar_libros_prestados_usuario("U001"):
        print(libro)

    # Buscar libros por autor "Raúl"
    print("\nBuscar libros por autor 'Raúl':")
    for libro in biblioteca.buscar_por_autor("Raúl"):
        print(libro)

    # Devolver libro
    biblioteca.devolver_libro("U001", "1234567890")

    # Intentar quitar libro prestado
    biblioteca.quitar_libro("0987654321")  # No se puede porque está prestado

    # Dar de baja usuario Jessica
    biblioteca.dar_baja_usuario("U001")

if __name__ == "__main__":
    main()