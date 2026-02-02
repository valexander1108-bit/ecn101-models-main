import numpy as np
from dataclasses import dataclass

@dataclass
class ADASParams:
    a: float = 100.0  # demand intercept
    b: float = 1.0    # demand slope (Y = a - b*P)
    y_star: float = 100.0  # potential output (LRAS)
    sras_slope: float = 0.5  # SRAS slope
    p_expected: float = 100.0  # expected price level


def ad_curve(P: np.ndarray, p: ADASParams):
    return p.a - p.b * P


def sras_curve(P: np.ndarray, p: ADASParams):
    # SRAS: Y = y* + s*(P - Pe)
    return p.y_star + p.sras_slope * (P - p.p_expected)


def lras_value(p: ADASParams):
    return p.y_star