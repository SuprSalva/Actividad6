"""Pruebas de sistema: se ejecuta main.py como programa completo, igual que lo haría un usuario."""

import os
import subprocess
import sys
from pathlib import Path

CARPETA = Path(__file__).parent


def ejecutar_programa(*argumentos):
    """Corre `python main.py <argumentos>` en otro proceso y regresa el resultado."""
    entorno = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, "main.py", *argumentos],
        cwd=CARPETA,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=entorno,
    )


# --- Camino del try: el programa termina bien (código de salida 0) ---

def test_sistema_try_venta_valida():
    resultado = ejecutar_programa("100", "20")
    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "Precio final: $92.80"


def test_sistema_try_con_iva_personalizado():
    resultado = ejecutar_programa("250", "10", "8")
    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "Precio final: $243.00"


# --- Camino del except: el programa avisa el error (código de salida 1) ---

def test_sistema_except_descuento_invalido():
    resultado = ejecutar_programa("100", "120")
    assert resultado.returncode == 1
    assert resultado.stdout == ""
    assert "Error: El porcentaje de descuento debe estar entre 0 y 100." in resultado.stderr


def test_sistema_except_texto_no_numerico():
    resultado = ejecutar_programa("abc", "10")
    assert resultado.returncode == 1
    assert "debe ser un número" in resultado.stderr


def test_sistema_uso_incorrecto_sin_datos():
    resultado = ejecutar_programa()
    assert resultado.returncode == 2
    assert "Uso: python main.py" in resultado.stderr
