
import gc
import weakref

from figuras import (
    Etiqueta,
    Lado,
    Triangulo,
    Cuadrado,
    Pentagono,
    Hexagono,
    Taller,
    exportar_todo,
    Poligono,
)
from libreria_externa import PlanoCAD


# Crear los cuatro polígonos
triangulo = Triangulo(
    "Triángulo", "rojo",
    [Lado(3, Etiqueta("Base")), Lado(4), Lado(5)]
)

cuadrado = Cuadrado(
    "Cuadrado", "azul",
    [Lado(2, Etiqueta("Lado principal")), Lado(2), Lado(2), Lado(2)]
)

pentagono = Pentagono(
    "Pentágono", "verde",
    [Lado(3) for _ in range(5)]
)

hexagono = Hexagono(
    "Hexágono", "amarillo",
    [Lado(2) for _ in range(6)]
)


# El Taller recibe objetos ya construidos
taller = Taller()

for poligono in [triangulo, cuadrado, pentagono, hexagono]:
    taller.recibir(poligono)


# Exportar polígonos y objeto externo con el mismo contrato
plano = PlanoCAD("PL-001")
elementos = taller.inventario() + [plano]

print("EXPORTACIÓN")
for resultado in exportar_todo(elementos):
    print(resultado)


# Mostrar inventario
print("\nINVENTARIO DEL TALLER")
for poligono in taller.inventario():
    print(f"- {poligono.nombre}: {len(poligono.lados())} lados")


# Comprobar que Poligono es abstracta
print("\nCLASE ABSTRACTA")
try:
    Poligono("Figura", "negro", [])
except TypeError as error:
    print("No se puede instanciar Poligono:", error)


# Composición: el Lado deja de existir al eliminar su Poligono
print("\nCOMPOSICIÓN")
lado = Lado(10)
lado_ref = weakref.ref(lado)
poligono_temporal = Triangulo(
    "Temporal", "gris",
    [lado, Lado(10), Lado(10)]
)

del lado
del poligono_temporal
gc.collect()

print("¿El lado dejó de existir?", lado_ref() is None)


# Agregación: el Poligono sobrevive al eliminar el Taller
print("\nAGREGACIÓN")
poligono_independiente = Cuadrado(
    "Independiente", "blanco",
    [Lado(1) for _ in range(4)]
)
poligono_ref = weakref.ref(poligono_independiente)

taller_temporal = Taller()
taller_temporal.recibir(poligono_independiente)

del taller_temporal
gc.collect()

print("¿El polígono sigue existiendo?", poligono_ref() is not None)
