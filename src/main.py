from src.config import TEMA
from src.dominio.biblioteca import Biblioteca, versiones_de

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

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

def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print(f"\n=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva (versiones derivadas)")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    biblioteca = Biblioteca()
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
        elif opcion in {"3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
