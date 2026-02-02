# models/solow.py — Minimal Solow transition dynamics (non-stochastic)
import numpy as np
from dataclasses import dataclass

@dataclass
class SolowParams:
    s: float = 0.2      # savings rate
    delta: float = 0.05 # depreciation
    n: float = 0.01     # population growth
    g: float = 0.02     # technology growth
    alpha: float = 0.33 # capital share

def solow_next_k(k: float, params: SolowParams) -> float:
    """
    Discrete-time capital per effective worker:
    k_{t+1} = [s * k_t^alpha + (1 - delta) * k_t] / (1 + n + g)
    """
    y = k ** params.alpha
    k_next = (params.s * y + (1 - params.delta) * k) / (1 + params.n + params.g)
    return k_next

def simulate_path(k0: float, T: int, params: SolowParams):
    k = np.zeros(T)
    k[0] = k0
    for t in range(T-1):
        k[t+1] = solow_next_k(k[t], params)
    y = k ** params.alpha
    return k, y
