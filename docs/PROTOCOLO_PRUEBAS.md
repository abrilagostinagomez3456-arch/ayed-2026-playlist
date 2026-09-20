# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
|---|---|---|---|---|---|---|
| P01 | E1 | Arrancar el programa y listar catálogo (opción 1) | dataset de la cátedra | lista no vacía, sin traceback | pasa | Verificado en E1 |
| P02 | E1 | Buscar un ítem inexistente (opción 2) | id = -1 | mensaje claro, el menú sigue | pasa | Verificado en E1 |
| P03 | E2 | Recursión sobre un ítem CON cadena (opción 5) | id = 1 ("De Musica Ligera") | imprime la versión derivada ID 62 | no corrido | Redactado para E2 |
| P04 | E2 | Recursión sobre un ítem SIN derivados (opción 5) | id = 2 ("Persiana Americana") | informa caso base sin derivados | no corrido | Redactado para E2 |
| P05 | E2 | Ver el detalle de un ítem que existe (opción 2) | id = 1 | muestra todos sus datos | no corrido | Redactado para E2 |
| P06 | E2 | Ver el detalle de un ítem que NO existe (opción 2) | id = 999 | mensaje claro, no se corta el programa | no corrido | Redactado para E2 |
| P07 | E2 | Elegir una opción de menú inválida | opción = "9z" | vuelve a mostrar el menú | no corrido | Redactado para E2 |
| P08 | E2 | Pasar enter vacío en el menú | enter vacío | no explota; vuelve a preguntar | no corrido | Redactado para E2 |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
