# cliente.py
# En este archivo se define la clase Cliente.
# Esta clase representa a una persona que compra libros en la tienda.

class Cliente:
    def __init__(self, nombre, email):
        # Constructor de la clase Cliente.
        # Se guardan los datos del cliente y se crea su carrito de compras.
        self.nombre = nombre
        self.email = email
        self.carrito = []  # Lista donde se guardan los libros que el cliente quiere comprar

    def agregar_al_carrito(self, libro, cantidad):
        # Este método permite agregar libros al carrito del cliente
        # Primero se verifica si hay suficiente stock del libro
        if libro.stock >= cantidad:
            # Se agrega el libro y la cantidad al carrito
            self.carrito.append((libro, cantidad))
            print(f"{cantidad} unidad(es) de '{libro.titulo}' agregadas al carrito.")
        else:
            # Si no hay stock suficiente, se informa al cliente
            print(f"No hay suficiente stock para '{libro.titulo}'.")

    def mostrar_carrito(self):
        # Este método muestra todos los libros que el cliente tiene en su carrito
        print(f"Carrito de {self.nombre}:")
        for libro, cantidad in self.carrito:
            print(f"- {libro.titulo} x {cantidad}")