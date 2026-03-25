from .Incidencias import *
from .IncidenciaHardware import *
from .IncidenciaSoftware import *


class Factory:

    _REGISTRO = {
        "hardware": IncidenciaHardware,
        "software": IncidenciaSoftware,
        "General": Incidencia
    }

    @classmethod
    def crear(cls, tipo, **kwargs):
        clase = cls._REGISTRO.get(tipo.strip().lower())

        if clase is None:
            raise ValueError(f"Tipo {tipo.strip().lower()} no existe")

        return clase(**kwargs)

    @classmethod
    def registrar(cls, nombre, clase):
        cls._REGISTRO[nombre] = clase