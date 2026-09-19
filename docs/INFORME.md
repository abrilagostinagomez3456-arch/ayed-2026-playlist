# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:Biblioteca Musical
- Por qué lo eligieron (5–8 líneas): Elegimos el tema de la biblioteca musical porque nos parece muy interesante y es el dominio que más utilizamos en nuestros sentimientos, ya que hay musica en todo lo que nos rodea. Además hay plataformas como Spotify o Youtube Music, nos resulta un sistema cercano e intuitivo para modelar este trabajo. 
## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.:
Cada ítem del catálogo es una cancion compuesta por atributos identificatorios (`id`, `titulo`, `artista`, `album`, `genero`, `anio`, `duracion_seg`). En esta primera etapa, cada registro utiliza campos de tipos inmutables (`int`, `str`) para garantizar la integridad de sus datos, modelados dentro de diccionarios que residen en una lista mutable (`list`) nativa para permitir la administración del catálogo en memoria. Hacia adelante, el catálogo actuará como repositorio base desde donde se seleccionarán elementos para armar la playlist (colección principal sobre `ListaEnlazada`), mientras que las reproducciones pasarán al Historial mediante una `Pila` (LIFO) y las canciones pendientes se programarán en la `Cola` de reproducción (FIFO).

## 3. Recursión (E2)

- Función: `obtener_versiones_derivadas_rec(id_origen, relaciones, catalogo_dict, nivel)` en `src/dominio/arbol_versiones.py`.
- Caso base: La canción consultada no posee derivaciones directas registradas (`derivadas_directas == []`), retornando una lista vacía `[]`.
- Caso recursivo:Itera sobre las derivaciones directas encontradas, añade la canción derivada al resultado e invoca a sí misma pasando el ID de la hija con `nivel + 1` para buscar derivaciones sucesivas.
- Traza de un ejemplo real del dataset (Canción ID 1: 'De Musica Ligera'):
1. Llamada inicial: `obtener_versiones_derivadas_rec(id_origen=1, nivel=1)`
   - Relación hallada: `cancion_id=62` ("De Musica Ligera (Unplugged)", tipo='live').
   - Registra a nivel 1 la canción 62.
2. Llamada recursiva: `obtener_versiones_derivadas_rec(id_origen=62, nivel=2)`
   - Busca derivadas donde `version_de_id == 62`. No existen.
   - Caso Base alcanzado: Retorna `[]`.
3. Retorno y resolución:
   - La llamada inicial une el resultado y retorna `[(1, Cancion(62), 'live')]`.

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
