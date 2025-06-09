# (Futuro) Clase Caño: representa un caño con sus propiedades
class Cano:
    def __init__(self, tipo_seccion, seccion, espesor, radio, dimensiones=6000):
        self.tipo_seccion = tipo_seccion
        self.seccion = seccion
        self.espesor = espesor
        self.radio = radio
        self.dimensiones = dimensiones
        self.nomenclatura = self.generar_nomenclatura()

    def generar_nomenclatura(self):
        return f"{self.tipo_seccion}-{self.seccion}-{self.espesor}-{self.radio}"
