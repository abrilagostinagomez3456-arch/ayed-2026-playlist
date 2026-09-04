from src.dominio.cancion import listar_catalogo

def menu():
    while True:
        print("\n=== Menú Playlist — AyED 2026 ===")
        print("1. Listar catálogo")
        print("2. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            listar_catalogo()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intentá de nuevo.")

if __name__ == "__main__":
    menu()