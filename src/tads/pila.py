from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """Pila implementada sobre ListaEnlazada (LIFO)."""
    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No hay canciones en el historial para desapilar.")
        tope = self.ver_tope()
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("El historial está vacío.")
        return self._items._cabeza.dato

    def esta_vacia(self) -> bool:
        return self._items.esta_vacia()
