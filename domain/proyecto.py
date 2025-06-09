# Clase Proyecto: representa un proyecto de corte
from datetime import datetime


class Proyecto:
    def __init__(self, nombre, cliente, fecha_creacion=None, productos=None):
        self.nombre = nombre
        self.cliente = cliente
        self.fecha_creacion = (
            fecha_creacion
            if fecha_creacion
            else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.productos = productos if productos is not None else []

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "cliente": self.cliente,
            "fecha_creacion": self.fecha_creacion,
            "productos": self.productos,
        }
