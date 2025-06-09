# Pruebas unitarias para Proyecto y componentes asociados
import unittest

class TestProyecto(unittest.TestCase):
    def test_creacion(self):
        from domain.proyecto import Proyecto
        p = Proyecto("Proyecto1", "Cliente1", "2025-06-08")
        self.assertEqual(p.nombre, "Proyecto1")

if __name__ == "__main__":
    unittest.main()
