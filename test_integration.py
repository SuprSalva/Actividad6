"""Pruebas de integración: main.py trabajando junto con las funciones de precios.py."""

import pytest
from main import procesar_venta
from precios import calcular_precio_final


# --- Camino del try: los módulos trabajan juntos y regresan el total ---

def test_integracion_try_venta_con_descuento_e_iva():
    # 100 con 20% de descuento = 80; 80 más 16% de IVA = 92.8
    resultado = procesar_venta(100, 20)
    assert resultado == {"exito": True, "total": 92.8}


def test_integracion_try_datos_como_texto():
    # Los datos llegan como texto (como desde la terminal) y se convierten antes de calcular.
    # 250 con 10% de descuento = 225; 225 más 8% de IVA = 243.0
    resultado = procesar_venta("250", "10", "8")
    assert resultado["exito"] is True
    assert resultado["total"] == 243.0


# --- Camino del except: el error de precios.py llega a main.py y se captura ---

def test_integracion_except_descuento_invalido():
    resultado = procesar_venta(100, 120)
    assert resultado["exito"] is False
    assert resultado["error"] == "El porcentaje de descuento debe estar entre 0 y 100."


def test_integracion_except_precio_negativo():
    resultado = procesar_venta(-50, 10)
    assert resultado["exito"] is False
    assert "precio no puede ser negativo" in resultado["error"]


def test_integracion_except_texto_no_numerico():
    resultado = procesar_venta("cien", 10)
    assert resultado["exito"] is False
    assert "debe ser un número" in resultado["error"]


def test_integracion_except_error_se_propaga_entre_funciones():
    # calcular_precio_final llama a calcular_descuento y a calcular_iva;
    # el ValueError de calcular_iva debe llegar hasta quien llamó.
    with pytest.raises(ValueError, match="IVA no puede ser negativo"):
        calcular_precio_final(100, 10, -16)
