# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
|---|---|---|---|---|---|---|
| P01 | E1 | Arrancar el programa y listar catálogo (opción 1) | dataset de la cátedra | lista no vacía, sin traceback | pasa | Verificado en E1 |
| P02 | E1 | Buscar un ítem inexistente (opción 2) | id = -1 | mensaje claro, el menú sigue | pasa | Verificado en E1 |
| P03 | E2 | Recursión sobre un ítem CON cadena (opción 5) | id = 1 ("De Musica Ligera") | imprime la versión derivada ID 62 (live) | pasa | Verificado en E2 / regresión E3 |
| P04 | E2 | Recursión sobre un ítem SIN derivados (opción 5) | id = 2 ("Persiana Americana") | informa caso base sin derivados | pasa | Verificado en E2 / regresión E3 |
| P05 | E3 | Agregar a la colección principal hasta el tope (opción 6 -> 1) | playlist de 6 temas; intentar agregar el 7mo | falla con ColeccionLlenaError capturada, menú sigue | pasa | Verificado en E3 |
| P06 | E3 | Desapilar historial vacío (opción 7 -> 2) | pila sin elementos previos | PilaVaciaError capturada, menú sigue | pasa | Verificado en E3 |
| P07 | E3 | Desencolar cola vacía (opción 8 -> 2) | cola sin elementos previos | ColaVaciaError capturada, menú sigue | pasa | Verificado en E3 |
| P08 | E3 | Listar colección con el iterador (opción 6 -> 2) | 2+ canciones agregadas a la playlist | el orden coincide con las inserciones | pasa | Verificado en E3 |
| P09 | E4 | Búsqueda lineal de un nombre que existe | | lo encuentra | no corrido | Para E4 |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | | no encontrado, sin traceback | no corrido | Para E4 |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | | avisa o reordena; no da un falso hit | no corrido | Para E4 |
| P12 | E4 | Ordenar por un criterio y después por otro | | el orden cambia | no corrido | Para E4 |
| P13 | E5 | Guardar texto (`.txt`), salir, volver a entrar | | los datos siguen | no corrido | Para E5 |
| P14 | E5 | Guardar binario y modificar un registro por id | | al recargar, ese campo cambió | no corrido | Para E5 |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido | Para E5 |
