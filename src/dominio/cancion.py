CATALOGO = [
    {"id": 1, "titulo": "De Música Ligera", "artista": "Soda Stereo", "duracion": "3:32"},
    {"id": 2, "titulo": "Ji Ji Ji", "artista": "Patricio Rey", "duracion": "5:30"},
    {"id": 3, "titulo": "Crimen", "artista": "Gustavo Cerati", "duracion": "3:52"},
]

def listar_catalogo():
    print("\n=== Catálogo de Canciones ===")
    for c in CATALOGO:
        print(f"[{c['id']}] {c['titulo']} - {c['artista']} ({c['duracion']})")
    print("=============================\n")