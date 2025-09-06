# libro.py

class Libro:
    """
    Libro con título y autor inmutables (tupla), categoría e ISBN.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.info[0]

    @property
    def autor(self):
        return self.info[1]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} [{self.categoria}] (ISBN: {self.isbn})"