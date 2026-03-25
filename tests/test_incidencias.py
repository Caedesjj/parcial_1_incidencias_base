"""Tests base del parcial de incidencias."""

from models import Incidencia, IncidenciaHardware, IncidenciaSoftware
from storage import guardar_incidencias_txt



def test_incidencia_base_tiene_atributos():
    incidencia = Incidencia("GEN-001", "Laura", "Descripción general")

    assert incidencia.codigo == "GEN-001"
    assert incidencia.usuario == "Laura"
    assert incidencia.descripcion == "Descripción general"



def test_incidencia_software_es_subclase():
    incidencia = IncidenciaSoftware(
        "SW-001",
        "Ana",
        "Error al abrir la aplicación",
        "VS Code",
    )

    assert isinstance(incidencia, Incidencia)
    assert incidencia.aplicacion == "VS Code"



def test_incidencia_hardware_es_subclase():
    incidencia = IncidenciaHardware(
        "HW-001",
        "Carlos",
        "No enciende el equipo",
        "Portátil",
    )

    assert isinstance(incidencia, Incidencia)
    assert incidencia.dispositivo == "Portátil"



def test_resumen_software_contiene_informacion_clave():
    incidencia = IncidenciaSoftware(
        "SW-001",
        "Ana",
        "Error al abrir la aplicación",
        "VS Code",
    )

    resumen = incidencia.resumen()

    assert "SW-001" in resumen
    assert "Ana" in resumen
    assert "VS Code" in resumen
    assert "Error al abrir la aplicación" in resumen



def test_resumen_hardware_contiene_informacion_clave():
    incidencia = IncidenciaHardware(
        "HW-001",
        "Carlos",
        "No enciende el equipo",
        "Portátil",
    )

    resumen = incidencia.resumen()

    assert "HW-001" in resumen
    assert "Carlos" in resumen
    assert "Portátil" in resumen
    assert "No enciende el equipo" in resumen



def test_guardar_incidencias_txt_crea_archivo(tmp_path):
    archivo = tmp_path / "salida.txt"

    incidencias = [
        IncidenciaSoftware(
            "SW-001",
            "Ana",
            "Error al abrir la aplicación",
            "VS Code",
        ),
        IncidenciaHardware(
            "HW-001",
            "Carlos",
            "No enciende el equipo",
            "Portátil",
        ),
    ]

    guardar_incidencias_txt(incidencias, archivo)

    assert archivo.exists()



def test_guardar_incidencias_txt_escribe_contenido(tmp_path):
    archivo = tmp_path / "salida.txt"

    incidencias = [
        IncidenciaSoftware(
            "SW-001",
            "Ana",
            "Error al abrir la aplicación",
            "VS Code",
        ),
        IncidenciaHardware(
            "HW-001",
            "Carlos",
            "No enciende el equipo",
            "Portátil",
        ),
    ]

    guardar_incidencias_txt(incidencias, archivo)

    contenido = archivo.read_text(encoding="utf-8")

    assert "SW-001" in contenido
    assert "HW-001" in contenido
    assert "VS Code" in contenido
    assert "Portátil" in contenido
