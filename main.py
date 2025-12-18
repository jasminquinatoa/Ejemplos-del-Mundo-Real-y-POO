# main.py
# Este archivo es el principal del programa.
# Aquí se crean los objetos y se prueba el funcionamiento de todas las clases.

from Libro import Libro
from cliente import Cliente
from tienda import Tienda

# Se crean algunos libros para la tienda
libro1 = Libro("Python Básico", "Ana Pérez", 25, 10)
libro2 = Libro("Matemáticas Avanzadas", "Juan Gómez", 40, 5)

# Se crea la tienda
mi_tienda = Tienda("Libros Online")

# Se agregan los libros al inventario
mi_tienda.agregar_libro(libro1)
mi_tienda.agregar_libro(libro2)

# Se muestra el inventario inicial
mi_tienda.mostrar_inventario()

# Se crea un cliente
cliente1 = Cliente("Luis Torres", "luis@example.com")

# El cliente agrega libros al carrito
cliente1.agregar_al_carrito(libro1, 2)
cliente1.agregar_al_carrito(libro2, 1)

# Se muestra el carrito del cliente
cliente1.mostrar_carrito()

# Se procesa la compra
mi_tienda.procesar_compra(cliente1)

# Se muestra el inventario actualizado después de la compra
mi_tienda.mostrar_inventario()