# Informe – TP Integrador Unidad 3: POO

## Parte 1. Diagnóstico de Java-ismos

| # | Java-ismo | Dónde | Inversión que lo explica | Síntoma observable |
|---|---|---|---|---|
| 1 | Getters sin lógica | `Figura.getNombre/getColor` | Acceso directo por convención | Métodos innecesarios |
| 2 | Getter/setter Java Bean | `Lado.getLongitud/setLongitud` | `@property` cuando hay validación | Acceso `lado.longitud` |
| 3 | Atributo de clase mutable | `Poligono.catalogo` | No imitar `static` sin necesidad | Registro compartido |
| 4 | Argumentos mutables por defecto | `Poligono.__init__` | Crear listas dentro del constructor | Dos objetos comparten observaciones |
| 5 | Omitir inicializador padre | `Poligono.__init__` | `super()` mantiene la inicialización heredada | Atributos base no inicializados |
| 6 | Guardar alias de lista | `Poligono.__init__` | Copia defensiva | Cambiar la lista externa modifica el polígono |
| 7 | Acumulador manual | `Poligono.perimetro` | Usar abstracciones propias del lenguaje | Código más extenso que `sum()` |
| 8 | Simular sobrecarga de constructores | `Triangulo/Cuadrado.__init__` | Un constructor explícito y argumentos claros | Ramas por cantidad y tipo de argumentos |

Los síntomas de argumentos mutables y alias se reproducen en `demo_sintomas.py`. La propiedad `longitud` reemplaza el getter y setter, manteniendo el acceso del cliente mediante `lado.longitud`.

## Equivalencias Java–Python

| Elemento Java | Cómo quedó Python | ¿Traducción directa o rediseño? | Por qué |
|---|---|---|---|
| Getters simples | Atributos públicos | Rediseño | No agregan lógica |
| Getter/setter validado | `@property` | Rediseño | Valida al asignar |
| `static` mutable | Sin catálogo global | Rediseño | Evita estado compartido innecesario |
| Constructor sobrecargado | Constructor explícito | Rediseño | Python no requiere sobrecarga |
| Interfaz | `Protocol` | Rediseño | Contrato estructural |
| Clase abstracta | `ABC` | Equivalencia conceptual | Expresa una jerarquía del dominio |
| Copia de colección | `list(...)` | Equivalencia conceptual | Evita exponer la lista interna |

## Parte 2. Relaciones

- **Taller–Polígono (agregación):** `Taller.recibir()` guarda un polígono recibido; no lo construye. El polígono puede existir sin el taller.
- **Polígono–Lado (composición):** el constructor de `Poligono` recibe y conserva los lados en `_lados`; estos forman parte de su estructura.
- **Lado–Etiqueta (asociación):** `Lado.__init__` recibe una etiqueta opcional (`Etiqueta` o `None`); no controla su ciclo de vida.

`Poligono.lados()` y `Taller.inventario()` devuelven copias defensivas de sus listas.

## Parte 3. Herencia

`Triangulo`, `Cuadrado`, `Pentagono` y `Hexagono` heredan de `Poligono` porque representan tipos concretos de polígono. `PoligonoRegular` también hereda de `Poligono`: es un polígono por definición del dominio. La herencia se justifica por la relación «es-un», no por la necesidad de compartir una lista. `Poligono` no puede instanciarse sin implementar `lados_esperados()`.

## Parte 4. ABC y Protocol

`Exportable` se implementa con `Protocol`. Tanto `Poligono` como `PlanoCAD` ofrecen `exportar()`, aunque `PlanoCAD` no hereda de nuestro código. Una ABC exigiría modificar la clase externa o adaptarla mediante herencia. La elección entre ABC y Protocol depende del dominio y del tipo de contrato buscado, no de una limitación del lenguaje.

## Cierre

Al pasar de Java a Python cambiaron los getters simples, los constructores, el manejo de colecciones y los contratos de tipo. Se mantuvieron las reglas del dominio: las figuras son polígonos, los polígonos tienen lados y cada subtipo valida su cantidad.
