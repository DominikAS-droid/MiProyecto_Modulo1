import math

# =========================================================
# FUNCIONES AUXILIARES
# =========================================================


def validar_positivo(valor: float, nombre: str, permitir_cero: bool = False) -> None:
    if permitir_cero:
        if valor < 0:
            raise ValueError(f"{nombre} no puede ser negativo.")
    else:
        if valor <= 0:
            raise ValueError(f"{nombre} debe ser mayor que cero.")


def validar_porcentaje(valor: float, nombre: str) -> None:
    if valor < 0 or valor > 100:
        raise ValueError(f"{nombre} debe estar entre 0 y 100.")


# =========================================================
# 4) ADMINISTRACIÓN / NEGOCIOS
# =========================================================


def calcular_punto_equilibrio(
    costos_fijos: float, precio_unitario: float, costo_variable_unitario: float
) -> dict:
    """
    Calcula el punto de equilibrio en unidades y en ventas.
    Fórmula:
    - margen de contribución = precio - costo variable
    - punto equilibrio unidades = costos fijos / margen contribución
    """
    validar_positivo(costos_fijos, "costos_fijos")
    validar_positivo(precio_unitario, "precio_unitario")
    validar_positivo(
        costo_variable_unitario, "costo_variable_unitario", permitir_cero=True
    )

    margen_contribucion = precio_unitario - costo_variable_unitario

    if margen_contribucion <= 0:
        raise ValueError(
            "El precio_unitario debe ser mayor que el costo_variable_unitario."
        )

    unidades = costos_fijos / margen_contribucion
    ventas = unidades * precio_unitario

    return {
        "margen_contribucion_unitario": round(margen_contribucion, 2),
        "punto_equilibrio_unidades": round(unidades, 2),
        "punto_equilibrio_ventas": round(ventas, 2),
    }
