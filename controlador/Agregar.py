
class Agregar:
    def agregar_incidencia(self):
        """Solicita los datos de una incidencia y la agrega a la lista."""

        self.tipo = input("Tipo (software/hardware): ").strip().lower()
        self.codigo = input("Código: ").strip()
        self.usuario = input("Usuario: ").strip()
        self.descripcion = input("Descripción: ").strip()
        self.extra = input("Aplicación o dispositivo: ").strip()

        return("Incidencia Agregada")


