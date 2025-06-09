# Clase Producto: representa un elemento dentro de un proyecto
class Producto:
    def __init__(self, nombre, cantidad, piezas=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.piezas = piezas if piezas is not None else []
