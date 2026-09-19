# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
|---|---|---|---|---|---|---|
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa | Verificado en E1 |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | pasa | Verificado en E1 |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | id = 1 ("De Musica Ligera") | imprime la versión derivada ID 62 (live) | no corrido | Redactado para E2 |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | id = 2 ("Persiana Americana") | mensaje informando caso base sin derivados | no corrido | Redactado para E2 |
| P05 | E3 | Agregar a la colección principal hasta el tope | playlist con más elementos del límite | falla con excepción propia de colección llena | no corrido | Para E3 |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia capturada, menú sigue | no corrido | Para E3 |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia capturada, menú sigue | no corrido | Para E3 |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | no corrido | Para E3 |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
