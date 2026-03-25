from Incidencias import Incidencia


class IncidenciaHardware(Incidencia):
    def __init__(self,  codigo, usuario, descripcion, extra):
        super().__init__( codigo, usuario, descripcion, extra)
        self.tipo = "Hardware"

