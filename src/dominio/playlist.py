from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, ColeccionVaciaError, ItemNoEncontradoError

class Playlist:
    """Colección principal con tope (límite máximo de 6 canciones) sobre ListaEnlazada."""
    def __init__(self, nombre: str = "Favoritas", tope: int = 6):
        self.nombre = nombre
        self._tope = tope
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        if self._canciones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"La playlist está llena (máximo {self._tope} canciones).")
        self._canciones.insertar_al_final(cancion)

    def eliminar(self, cancion):
        if self._canciones.esta_vacia():
            raise ColeccionVaciaError("La playlist está vacía.")
        eliminado = self._canciones.eliminar(cancion)
        if not eliminado:
            raise ItemNoEncontradoError(f"La canción {cancion.titulo} no está en la playlist.")

    def esta_vacia(self) -> bool:
        return self._canciones.esta_vacia()

    def tamanio(self) -> int:
        return self._canciones.tamanio()

    def __iter__(self):
        """Usa el iterador propio de ListaEnlazada respetando el encapsulamiento."""
        return iter(self._canciones)
