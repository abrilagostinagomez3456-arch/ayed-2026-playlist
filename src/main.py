# src/main.py
from src.config import TEMA
from src.catalogo import obtener_canciones, buscar_cancion_por_id

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def listar_catalogo():
    """Operación 1 (Protocolo P01)."""
    canciones = obtener_canciones()
    print("\n--- CATÁLOGO DE CANCIONES ---")
    print(f"{'ID':<4} | {'Título':<32} | {'Artista':<26} | {'Año':<4}")
    print("-" * 72)
    for c in canciones:
        print(f"{c['id']:<4} | {c['titulo']:<32} | {c['artista']:<26} | {c['anio']:<4}")
    print(f"\nTotal: {len(canciones)} canciones.")


def ver_detalle():
    """Operación 2 (Protocolo P02)."""
    entrada = input("\nIngrese el ID de la canción: ").strip()
    es_entero = entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())
    if not es_entero:
        print("Error: El ID debe ser un número entero.")
        return

    cancion = buscar_cancion_por_id(int(entrada))
    if cancion:
        print("\n--- DETALLE DE LA CANCIÓN ---")
        for clave, valor in cancion.items():
            print(f"{clave.capitalize():<14}: {valor}")
    else:
        print(f"Aviso: No existe ninguna canción con el ID {entrada}.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print(f"\n=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo()
        elif opcion == "2":
            ver_detalle()
        elif opcion in {"3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
