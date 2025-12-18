# libro.py
# En este archivo se define la clase Libro.
# Esta clase representa un libro real que se vende en una tienda.

class Libro:
    def __init__(self, titulo, autor, precio, stock):
        # Constructor de la clase Libro.
        # Aquí se inicializan los datos principales del libro.
        self.titulo = titulo      # Nombre del libro
        self.autor = autor        # Autor del libro
        self.precio = precio      # Precio del libro en dólares
        self.stock = stock        # Cantidad disponible en la tienda

    def mostrar_info(self):
        # Este método muestra la información del libro de forma clara
        print(f"'{self.titulo}' de {self.autor} - ${self.precio} (Stock: {self.stock})")

    def vender(self, cantidad):
        # Este método se usa cuando se vende un libro
        # Primero se verifica si hay suficiente stock
        if cantidad <= self.stock:
            self.stock -= cantidad  # Se reduce el stock
            print(f"Se han vendido {cantidad} unidad(es) de '{self.titulo}'.")
        else:
            # Si no hay stock suficiente, se muestra un mensaje
            print(f"No hay suficiente stock de '{self.titulo}'.")