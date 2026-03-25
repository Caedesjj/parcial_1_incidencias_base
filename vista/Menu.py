
from controlador.Agregar import Agregar
from controlador.Resumen import Resumen
from almacen.Persistencia import Guardar

class Menu:
    def __init__(self):
        self.incidencias = []
        self.agregar = Agregar()
        self.resumen = Resumen()
        self.guardar = Guardar()

    def mostrar_menu(self):
        while True:
            print("\n--- Sistema de incidencias ---")
            print("1. Agregar incidencia")
            print("2. Mostrar incidencias")
            print("3. Guardar incidencias")
            print("4. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                incidencia = self.agregar.agregar_incidencia()
                self.incidencias.append(incidencia)
                print("Incidencia registrada.")
            elif opcion == "2":
                if not self.incidencias:
                    print("No hay incidencias.")
                for i in self.incidencias:
                    print(self.resumen.obtener_resumen(i))
            elif opcion == "3":
                self.guardar.guardar_incidencias(self.incidencias)
            elif opcion == "4":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida.")