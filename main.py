"""Programa principal: calcula el precio final de una venta con las funciones de precios.py.

Uso desde la terminal:
    python main.py <precio> <descuento> [iva]
"""

import sys

from precios import calcular_precio_final


def convertir_numero(valor, nombre: str) -> float:
    """Convierte un valor (texto o número) a float con un mensaje de error en español."""
    try:
        return float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"El {nombre} debe ser un número, se recibió: {valor!r}.")


def procesar_venta(precio, porcentaje_descuento, porcentaje_iva=16.0) -> dict:
    """Procesa una venta: aplica el descuento y después el IVA.

    Si los datos son válidos, el cálculo termina dentro del try y se regresa el total.
    Si algo es inválido, el except captura el ValueError y se regresa el mensaje de error.
    """
    try:
        precio = convertir_numero(precio, "precio")
        porcentaje_descuento = convertir_numero(porcentaje_descuento, "descuento")
        porcentaje_iva = convertir_numero(porcentaje_iva, "IVA")
        total = calcular_precio_final(precio, porcentaje_descuento, porcentaje_iva)
    except ValueError as error:
        return {"exito": False, "error": str(error)}
    return {"exito": True, "total": total}


def main(argumentos=None) -> int:
    """Lee los datos de la línea de comandos, muestra el resultado y regresa el código de salida."""
    if argumentos is None:
        argumentos = sys.argv[1:]

    if len(argumentos) not in (2, 3):
        print("Uso: python main.py <precio> <descuento> [iva]", file=sys.stderr)
        return 2

    resultado = procesar_venta(*argumentos)
    if resultado["exito"]:
        print(f"Precio final: ${resultado['total']:.2f}")
        return 0

    print(f"Error: {resultado['error']}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
