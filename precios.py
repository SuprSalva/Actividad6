"""Funciones para calcular precios con descuentos e IVA."""


def calcular_descuento(precio: float, porcentaje_descuento: float) -> float:
    """Calcula el precio final después de aplicar un porcentaje de descuento."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

    descuento = precio * (porcentaje_descuento / 100)
    return round(precio - descuento, 2)


def calcular_iva(precio: float, porcentaje_iva: float = 16.0) -> float:
    """Calcula el precio total sumando el porcentaje de IVA (16% por defecto)."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if porcentaje_iva < 0:
        raise ValueError("El porcentaje de IVA no puede ser negativo.")

    iva = precio * (porcentaje_iva / 100)
    return round(precio + iva, 2)


def calcular_precio_final(
    precio: float, porcentaje_descuento: float, porcentaje_iva: float = 16.0
) -> float:
    """Calcula el precio aplicando primero el descuento y después el IVA."""
    precio_con_descuento = calcular_descuento(precio, porcentaje_descuento)
    return calcular_iva(precio_con_descuento, porcentaje_iva)
