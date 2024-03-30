# Tarea semana 14
# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=12):
    """
    Calcula el descuento aplicado al monto total de la compra.

    Parámetros:
        - monto_total: El monto total de la compra.
        - porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10%).

    Retorna:
        El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función calcular_descuento
monto_compra_1 = 1000
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
monto_compra_2 = 2000
porcentaje_descuento_2 = 22
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Mostrar los resultados
print("Compra 1:")
print("Monto de la compra:", monto_compra_1)
print("Descuento aplicado:", descuento_1)
print("Monto final a pagar:", monto_final_1)

print("\nCompra 2:")
print("Monto de la compra:", monto_compra_2)
print("Descuento aplicado:", descuento_2)
print("Monto final a pagar:", monto_final_2)
