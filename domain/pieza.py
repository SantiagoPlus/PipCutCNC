# Clase Pieza: representa una pieza asociada a un producto
class Pieza:
    def __init__(self, nombre, cantidad, cano):
        self.nombre = nombre
        self.cantidad = cantidad
        self.cano = cano  # Instancia de Caño
