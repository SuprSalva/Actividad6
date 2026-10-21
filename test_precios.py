"""Set de pruebas con pytest para las funciones de precios, descuentos e IVA."""

import pytest
from precios import calcular_descuento, calcular_iva, calcular_precio_final


def test_calcular_descuento():
    assert calcular_descuento(100, 20) == 80.0
    assert calcular_descuento(250, 10) == 225.0


def test_calcular_descuento_limites():
    assert calcular_descuento(150, 0) == 150.0
    assert calcular_descuento(150, 100) == 0.0


def test_calcular_iva_por_defecto():
    assert calcular_iva(100) == 116.0
    assert calcular_iva(50) == 58.0


def test_calcular_iva_personalizado():
    assert calcular_iva(200, 8) == 216.0
    assert calcular_iva(100, 0) == 100.0


def test_calcular_precio_final():
    # 100 con 20% de descuento = 80; 80 más 16% de IVA = 92.8
    assert calcular_precio_final(100, 20, 16) == 92.8


def test_errores_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_descuento(-50, 10)
    with pytest.raises(ValueError):
        calcular_descuento(100, 120)
    with pytest.raises(ValueError):
        calcular_iva(-10, 16)
