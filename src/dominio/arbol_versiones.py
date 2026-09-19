def obtener_versiones_derivadas_rec(id_origen: int, relaciones: list, catalogo_dict: dict, nivel: int = 1) -> list:
    """
    Función recursiva sobre el árbol de versiones.
    Caso base: si la canción evaluada no tiene versiones derivadas directas,
    retorna lista vacía [].
    Caso recursivo: recopila cada hija y se invoca a sí misma para sus sub-versiones.
    """
    derivadas_directas = [r for r in relaciones if r.version_de_id == id_origen]

    # Caso base
    if not derivadas_directas:
        return []

    resultado = []
    # Caso recursivo
    for rel in derivadas_directas:
        cancion_hija = catalogo_dict.get(rel.cancion_id)
        if cancion_hija:
            resultado.append((nivel, cancion_hija, rel.tipo))
            # Llamada recursiva profundizando un nivel
            sub_derivadas = obtener_versiones_derivadas_rec(
                cancion_hija.id, relaciones, catalogo_dict, nivel + 1
            )
            resultado.extend(sub_derivadas)

    return resultado