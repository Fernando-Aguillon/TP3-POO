import math


"""Dominio Figura / Polígono / Lado con Python idiomático."""

class Figura:
    def __init__(self, nombre, color):
        self._nombre = nombre
        self._color = color

    def area(self):
        return 0.0


class Lado:
    def __init__(self, longitud):
        self.longitud = longitud

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, valor):
        if valor <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = valor


class Poligono(Figura):
    def __init__(self, nombre, color, lados=None, observaciones=None):
        super().__init__(nombre, color)

        self._lados = list(lados) if lados is not None else []
        self._observaciones = (
            list(observaciones) if observaciones is not None else []
        )

    def lados_esperados(self):
        return 0

    def perimetro(self):
        return sum(lado.longitud for lado in self._lados)

    def area(self) -> str:
        return "Área sin calcular"

    def agregar_observacion(self, texto):
        self._observaciones.append(texto)

    def lados(self):
        return list(self._lados)


class Triangulo(Poligono):
    def lados_esperados(self):
        return 3


class Cuadrado(Poligono):
    def lados_esperados(self):
        return 4


class PoligonoRegular(Poligono):
    """Polígono de N lados de igual longitud.

    Su relación de herencia se revisará en la Parte 3.
    """

    def __init__(self, nombre, color, medida, cantidad):
        lados = [Lado(medida) for _ in range(cantidad)]
        super().__init__(nombre, color, lados)
        self._cantidad = cantidad

    def lados_esperados(self):
        return self._cantidad


if __name__ == "__main__":
    triangulo = Triangulo(
        "Triángulo",
        "rojo",
        [Lado(3), Lado(4), Lado(5)]
    )

    cuadrado = Cuadrado(
        "Cuadrado",
        "azul",
        [Lado(2), Lado(2), Lado(2), Lado(2)]
    )

    triangulo.agregar_observacion("Revisar el vértice A")

    print(f"Perímetro del triángulo: {triangulo.perimetro()}")
    print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")

    print(f"Nombre: {triangulo._nombre}")

    # Antes: lado.getLongitud()
    # Ahora: lado.longitud
    print(f"Longitud del primer lado: {triangulo.lados()[0].longitud}")

    regular = PoligonoRegular("Pentágono", "verde", 4, 5)
    print(f"Perímetro del pentágono: {regular.perimetro()}")