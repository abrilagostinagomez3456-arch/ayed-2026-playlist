from src.config import TEMA
from src.catalogo import obtener_catalogo, buscar_por_id, consultar_versiones_recursivo

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo():
    print("\n--- CATÁLOGO DE CANCIONES ---")
    print(f"{'ID':<4} | {'Título':<32} | {'Artista':<26} | {'Año':<4}")
    print("-" * 72)
    for c in obtener_catalogo():
        print(f"{c.id:<4} | {c.titulo:<32} | {c.artista:<26} | {c.anio:<4}")
    print(f"\nTotal: {len(obtener_catalogo())} canciones.")

def ver_detalle():
    entrada = input("\nIngrese el ID de la canción: ").strip()
    if not (entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit())):
        print("Error: El ID debe ser un número entero.")
        return
    c = buscar_por_id(int(entrada))
    if c:
        print("\n--- DETALLE DE LA CANCIÓN ---")
        print(c.detalle_completo())
    else:
        print(f"Aviso: No existe ninguna canción con el ID {entrada}.")

def operacion_recursiva():
    entrada = input("\nIngrese el ID de la canción base para buscar versiones derivadas: ").strip()
    if not entrada.isdigit():
        print("Error: Ingrese un ID numérico válido.")
        return
    cancion_id = int(entrada)
    origen = buscar_por_id(cancion_id)
    if not origen:
        print(f"Aviso: Canción {cancion_id} no encontrada.")
        return

    print(f"\nCanción base: {origen.titulo} ({origen.artista})")
    derivadas = consultar_versiones_recursivo(cancion_id)
    if not derivadas:
        print("-> No posee versiones derivadas registradas (caso base alcanzado).")
    else:
        print("Versiones encontradas:")
        for nivel, deriv, tipo in derivadas:
            indent = "  " * nivel
            print(f"{indent}└── [{tipo.upper()}] ID {deriv.id}: {deriv.titulo} - {deriv.artista} ({deriv.anio})")

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
        elif opcion == "5":
            operacion_recursiva()
        elif opcion in {"3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
