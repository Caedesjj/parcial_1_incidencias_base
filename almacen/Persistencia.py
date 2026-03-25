from controlador.Resumen import Resumen

class Guardar:
    def guardar_incidencias(self, incidencias):
        resumen = Resumen()
        with open("incidencias.txt", "w", encoding="utf-8") as archivo:
            for incidencia in incidencias:
                archivo.write(resumen.obtener_resumen(incidencia) + "\n")
        print("Incidencias guardadas en incidencias.txt")