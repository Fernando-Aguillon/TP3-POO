
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class Exportable(Protocol):
    def exportar(self) -> str:
        ...


@dataclass(frozen=True)
class Etiqueta:
    texto: str


class Figura(ABC):
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    @abstractmethod
    def area(self) -> float:
        pass


class Lado:
    def __init__(self, longitud, etiqueta=None):
        self.longitud = longitud
        self.etiqueta = etiqueta

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, valor):
        if valor <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = valor

    def escalar(self, factor):
        if factor <= 0:
            raise ValueError("El factor debe ser positivo")
        self.longitud *= factor


class Poligono(Figura, ABC):
    def __init__(self, nombre, color, lados):
        super().__init__(nombre, color)
        if len(lados) != self.lados_esperados():
            raise ValueError("Cantidad de lados incorrecta")
        self._lados = list(lados)

    @abstractmethod
    def lados_esperados(self):
        pass

    def perimetro(self):
        return sum(lado.longitud for lado in self._lados)
    
    def area(self):
        return 0.0

    def lados(self):
        return list(self._lados)

    def exportar(self):
        return f"{self.nombre}: perímetro {self.perimetro()}"


class Triangulo(Poligono):
    def lados_esperados(self):
        return 3

    def area(self):
        return 0.0


class Cuadrado(Poligono):
    def lados_esperados(self):
        return 4

    def area(self):
        return 0.0


class Pentagono(Poligono):
    def lados_esperados(self):
        return 5

    def area(self):
        return 0.0


class Hexagono(Poligono):
    def lados_esperados(self):
        return 6

    def area(self):
        return 0.0



class PoligonoRegular(Poligono):
    def __init__(self, nombre, color, medida, cantidad):
        self._cantidad = cantidad
        lados = [Lado(medida) for _ in range(cantidad)]
        super().__init__(nombre, color, lados)

    def lados_esperados(self):
        return self._cantidad

    def area(self):
        return 0.0



class Taller:
    def __init__(self):
        self._poligonos = []

    def recibir(self, poligono):
        self._poligonos.append(poligono)

    def restaurar(self, poligono):
        if poligono in self._poligonos:
            self._poligonos.remove(poligono)

    def inventario(self):
        return list(self._poligonos)


def exportar_todo(items: list[Exportable]) -> list[str]:
    return [item.exportar() for item in items]
