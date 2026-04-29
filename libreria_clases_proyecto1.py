import math

# =========================================================
# FUNCIONES AUXILIARES
# =========================================================


def validar_positivo(valor, nombre, permitir_cero=False):
    """Valida que un valor sea positivo."""
    if permitir_cero:
        if valor < 0:
            raise ValueError(f"{nombre} no puede ser negativo.")
    else:
        if valor <= 0:
            raise ValueError(f"{nombre} debe ser mayor que cero.")


def validar_porcentaje(valor, nombre):
    """Valida que un porcentaje esté entre 0 y 100."""
    if valor < 0 or valor > 100:
        raise ValueError(f"{nombre} debe estar entre 0 y 100.")


# =========================================================
# 2) FINANZAS
# =========================================================


class ProyectoInversion:
    """
    Representa un proyecto de inversión y permite calcular
    VPN, ROI y Payback simple.
    """

    def __init__(self, nombre_proyecto, inversion_inicial, flujos, tasa_descuento_pct):
        self.nombre_proyecto = nombre_proyecto
        self.inversion_inicial = inversion_inicial
        self.flujos = flujos
        self.tasa_descuento_pct = tasa_descuento_pct

        validar_positivo(self.inversion_inicial, "inversion_inicial")
        validar_porcentaje(self.tasa_descuento_pct, "tasa_descuento_pct")

        if not isinstance(self.flujos, list) or len(self.flujos) == 0:
            raise ValueError("flujos debe ser una lista con al menos un valor.")

    def calcular_vpn(self):
        tasa = self.tasa_descuento_pct / 100
        vpn = -self.inversion_inicial

        for periodo, flujo in enumerate(self.flujos, start=1):
            vpn += flujo / ((1 + tasa) ** periodo)

        return vpn

    def calcular_roi(self):
        utilidad_neta = sum(self.flujos) - self.inversion_inicial
        return (utilidad_neta / self.inversion_inicial) * 100

    def calcular_payback_simple(self):
        flujo_promedio = sum(self.flujos) / len(self.flujos)
        return self.inversion_inicial / flujo_promedio

    def resumen(self):
        vpn = self.calcular_vpn()
        return {
            "proyecto": self.nombre_proyecto,
            "vpn": round(vpn, 2),
            "roi_pct": round(self.calcular_roi(), 2),
            "payback_anios": round(self.calcular_payback_simple(), 2),
            "decision": "Viable" if vpn > 0 else "No viable",
        }
