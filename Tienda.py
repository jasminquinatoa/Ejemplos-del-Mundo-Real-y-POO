# tienda.py
# En este archivo se define la clase Tienda.
# Esta clase representa la tienda de libros y su funcionamiento.

class Tienda:
    def __init__(self, nombre):
        # Constructor de la clase Tienda.
        # Se inicializa el nombre de la tienda y su inventario.
        self.nombre = nombre
        self.inventario = []  # Lista donde se guardan los libros disponibles

    def agregar_libro(self, libro):
        # Este método permite agregar un libro al inventario de la tienda
        self.inventario.append(libro)
        print(f"Libro '{libro.titulo}' agregado al inventario.")

    def mostrar_inventario(self):
        # Este método muestra todos los libros disponibles en la tienda
        print(f"Inventario de la tienda '{self.nombre}':")
        for libro in self.inventario:
            libro.mostrar_info()  # Llama al método del libro para mostrar su información

    def procesar_compra(self, cliente):
        # Este método procesa la compra de un cliente
        # Calcula el total a pagar y actualiza el inventario
        total = 0
        for libro, cantidad in cliente.carrito:
            if libro.stock >= cantidad:
                libro.vender(cantidad)  # Se vende el libro
                total += libro.precio * cantidad  # Se suma al total
            else:
                print(f"No se pudo vender '{libro.titulo}' por falta de stock.")
        print(f"Total a pagar por {cliente.nombre}: ${total}")