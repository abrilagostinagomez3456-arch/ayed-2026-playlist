# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:Biblioteca Musical
- Por qué lo eligieron (5–8 líneas): Elegimos el tema de la biblioteca musical porque nos parece muy interesante y es el dominio que más utilizamos en nuestros sentimientos, ya que hay musica en todo lo que nos rodea. Además hay plataformas como Spotify o Youtube Music, nos resulta un sistema cercano e intuitivo para modelar este trabajo. 
## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.:
Cada ítem del catálogo es una cancion compuesta por atributos identificatorios (`id`, `titulo`, `artista`, `album`, `genero`, `anio`, `duracion_seg`). En esta primera etapa, cada registro utiliza campos de tipos inmutables (`int`, `str`) para garantizar la integridad de sus datos, modelados dentro de diccionarios que residen en una lista mutable (`list`) nativa para permitir la administración del catálogo en memoria. Hacia adelante, el catálogo actuará como repositorio base desde donde se seleccionarán elementos para armar la playlist (colección principal sobre `ListaEnlazada`), mientras que las reproducciones pasarán al Historial mediante una `Pila` (LIFO) y las canciones pendientes se programarán en la `Cola` de reproducción (FIFO).

## 3. Recursión (E2)
Función: `versiones_de(versionable, id_cancion)` en `src/dominio/biblioteca.py`.
Caso base: Si la canción evaluada no posee derivaciones directas (`if not directas:`), retorna `[]`.
Caso recursivo: Obtiene las versiones directas, las agrega al resultado y ejecuta recursivamente `versiones_de(versionable, v)` acumulando las sub-versiones.

Traza para 'De Musica Ligera' (id 1): según `versiones.csv`, 62 es versión directa de 1.
- Llamada 1: `versiones_de(biblioteca, 1)`
  - `directas = [62]`
  - `resultado = [62] + versiones_de(biblioteca, 62)`
- Llamada 2: `versiones_de(biblioteca, 62)`
  - `directas = []` (caso base: la canción 62 no tiene derivados)
  - Devuelve `[]`
- Resultado final: `[62] + [] = [62]` (Canción ID 62: "De Musica Ligera (Unplugged)").

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
