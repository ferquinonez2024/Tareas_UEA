# CalculoDescuentoPython.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.

    Args:
    - monto_total: float. Monto total de la compra.
    - porcentaje_descuento: float. Porcentaje de descuento a aplicar (por defecto 10%).

    Returns:
    - float. Monto del descuento calculado.
    """
    descuento = monto_total * porcentaje_descuento / 100
    return descuento


# Ejemplos de llamadas a la función
if __name__ == "__main__":
    # Llamada 1: Proporcionando solo el monto total de la compra
    monto_compra_1 = 100
    descuento_1 = calcular_descuento(monto_compra_1)
    print("Monto del descuento:", descuento_1)
    print("Monto final a pagar:", monto_compra_1 - descuento_1)

    # Llamada 2: Proporcionando tanto el monto total de la compra como el porcentaje de descuento
    monto_compra_2 = 200
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    print("\nMonto del descuento:", descuento_2)
    print("Monto final a pagar:", monto_compra_2 - descuento_2)
