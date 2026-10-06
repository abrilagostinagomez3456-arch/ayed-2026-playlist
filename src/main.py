from src.config import TEMA
from src.dominio.biblioteca import Biblioteca, versiones_de
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError
)

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def listar_catalogo(biblioteca: Biblioteca):
    print("\n--- CATÁLOGO DE CANCIONES ---")
    print(f"{'ID':<4} | {'Título':<32} | {'Artista':<26} | {'Año':<4}")
    print("-" * 72)
    for c in biblioteca.listar():
        print(f"{c.id:<4} | {c.titulo:<32} | {c.artista:<26} | {c.anio:<4}")
    print(f"\nTotal: {len(biblioteca.listar())} canciones.")

def ver_detalle(biblioteca: Biblioteca):
    entrada = input("\nIngrese el ID de la canción: ").strip()
    if not (entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())):
        print("Error: El ID debe ser un número entero.")
        return
    c = biblioteca.buscar(int(entrada))
    if c:
        print("\n--- DETALLE DE LA CANCIÓN ---")
        print(c.detalle_completo())
    else:
        print(f"Aviso: No existe ninguna canción con el ID {entrada}.")

def operacion_recursiva(biblioteca: Biblioteca):
    entrada = input("\nIngrese el ID de la canción base: ").strip()
    if not entrada.isdigit():
        print("Error: Ingrese un ID numérico válido.")
        return
    cancion_id = int(entrada)
    origen = biblioteca.buscar(cancion_id)
    if not origen:
        print(f"Aviso: Canción con ID {cancion_id} no encontrada.")
        return

    print(f"\nCanción base: {origen.titulo} ({origen.artista})")
    derivadas_ids = versiones_de(biblioteca, cancion_id)
    if not derivadas_ids:
        print("-> No posee versiones derivadas (caso base alcanzado).")
    else:
        print(f"Versiones derivadas encontradas (IDs {derivadas_ids}):")
        for v_id in derivadas_ids:
            c = biblioteca.buscar(v_id)
            if c:
                print(f"  └── [{c.id}] {c.titulo} - {c.artista} ({c.anio})")

def gestionar_playlist(playlist: Playlist, biblioteca: Biblioteca):
    print(f"\n--- PLAYLIST: {playlist.nombre} ({playlist.tamanio()}/6) ---")
    print("1. Agregar canción a la playlist")
    print("2. Listar canciones de la playlist (usa iterador)")
    print("0. Volver")
    op = input("> ").strip()
    if op == "1":
        entrada = input("ID de la canción: ").strip()
        if not entrada.isdigit():
            print("Error: Debe ingresar un ID numérico.")
            return
        cancion = biblioteca.buscar(int(entrada))
        if not cancion:
            print("Error: Canción no encontrada en el catálogo.")
            return
        try:
            playlist.agregar(cancion)
            print(f"Agregada: {cancion.titulo}")
        except ColeccionLlenaError as e:
            print(f"Error: {e}")
    elif op == "2":
        if playlist.esta_vacia():
            print("La playlist está vacía.")
            return
        print(f"\nCanciones en '{playlist.nombre}':")
        for c in playlist:  # Usa iterador propio
            print(f" • [{c.id}] {c.titulo} - {c.artista}")

def gestionar_historial(historial: Pila, biblioteca: Biblioteca):
    print("\n--- HISTORIAL DE REPRODUCCIÓN (PILA - LIFO) ---")
    print("1. Reproducir canción (apilar)")
    print("2. Deshacer última reproducción (desapilar)")
    print("3. Ver canción en la cima del historial (ver tope)")
    print("0. Volver")
    op = input("> ").strip()
    if op == "1":
        entrada = input("ID de la canción reproducida: ").strip()
        if not entrada.isdigit():
            print("Error: Debe ingresar un ID numérico.")
            return
        cancion = biblioteca.buscar(int(entrada))
        if not cancion:
            print("Error: Canción no encontrada.")
            return
        historial.apilar(cancion)
        print(f"Reproduciendo y apilando: {cancion.titulo}")
    elif op == "2":
        try:
            cancion = historial.desapilar()
            print(f"Desapilada del historial: {cancion.titulo}")
        except PilaVaciaError as e:
            print(f"Error: {e}")
    elif op == "3":
        try:
            cancion = historial.ver_tope()
            print(f"Tope actual: {cancion.titulo}")
        except PilaVaciaError as e:
            print(f"Error: {e}")

def gestionar_cola(cola: Cola, biblioteca: Biblioteca):
    print("\n--- COLA DE REPRODUCCIÓN (COLA - FIFO) ---")
    print("1. Encolar canción")
    print("2. Reproducir siguiente en fila (desencolar)")
    print("3. Ver próxima en fila (ver frente)")
    print("0. Volver")
    op = input("> ").strip()
    if op == "1":
        entrada = input("ID de la canción a encolar: ").strip()
        if not entrada.isdigit():
            print("Error: Debe ingresar un ID numérico.")
            return
        cancion = biblioteca.buscar(int(entrada))
        if not cancion:
            print("Error: Canción no encontrada.")
            return
        cola.encolar(cancion)
        print(f"Encolada: {cancion.titulo}")
    elif op == "2":
        try:
            cancion = cola.desencolar()
            print(f"Reproduciendo desde la cola: {cancion.titulo}")
        except ColaVaciaError as e:
            print(f"Error: {e}")
    elif op == "3":
        try:
            cancion = cola.ver_frente()
            print(f"Próxima en turno: {cancion.titulo}")
        except ColaVaciaError as e:
            print(f"Error: {e}")

def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print(f"\n=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva (versiones derivadas)")
    print("6. Colección principal (Playlist con tope)")
    print("7. Historial (pila)")
    print("8. Cola de reproducción")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    biblioteca = Biblioteca()
    playlist = Playlist(nombre="Favoritas", tope=6)
    historial = Pila()
    cola_reproduccion = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo(biblioteca)
        elif opcion == "2":
            ver_detalle(biblioteca)
        elif opcion == "5":
            operacion_recursiva(biblioteca)
        elif opcion == "6":
            gestionar_playlist(playlist, biblioteca)
        elif opcion == "7":
            gestionar_historial(historial, biblioteca)
        elif opcion == "8":
            gestionar_cola(cola_reproduccion, biblioteca)
        elif opcion in {"3", "4", "9"}:
            print("Todavía no está implementado. Corresponde a entregas posteriores.")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
