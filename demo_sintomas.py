"""Demostración de dos síntomas del diseño original."""


class PoligonoAnterior:
    def __init__(self, lados=[], observaciones=[]):
        self._lados = lados
        self._observaciones = observaciones


print("SÍNTOMA 1: argumento mutable compartido")

poligono_1 = PoligonoAnterior()
poligono_2 = PoligonoAnterior()

print(
    "¿Comparten las observaciones?",
    poligono_1._observaciones is poligono_2._observaciones
)

poligono_1._observaciones.append("Revisar figura")

print("Observaciones del polígono 1:", poligono_1._observaciones)
print("Observaciones del polígono 2:", poligono_2._observaciones)


print("\nSÍNTOMA 2: alias de una lista recibida")

lados_originales = [3, 4, 5]
poligono_3 = PoligonoAnterior(lados_originales)

print(
    "¿Comparten la misma lista?",
    poligono_3._lados is lados_originales
)

lados_originales.append(6)

print("Lista original:", lados_originales)
print("Lados del polígono:", poligono_3._lados)