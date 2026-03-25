

class Resumen:
    def obtener_resumen(self, incidencia):
        return f"[{incidencia.tipo.upper()}] {incidencia.codigo} - {incidencia.usuario} - {incidencia.extra} - {incidencia.descripcion}"