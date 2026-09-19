class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.artista} ({self.anio})"

    def detalle_completo(self) -> str:
        return (
            f"ID:       {self.id}\n"
            f"Título:   {self.titulo}\n"
            f"Artista:  {self.artista}\n"
            f"Álbum:    {self.album}\n"
            f"Género:   {self.genero}\n"
            f"Año:      {self.anio}\n"
            f"Duración: {self.duracion_seg} seg"
        )
