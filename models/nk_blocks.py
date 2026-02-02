import numpy as np
from dataclasses import dataclass

@dataclass
class NKParams:
    sigma: float = 1.0   # intertemporal elasticity
    beta: float = 0.99   # discount
    kappa: float = 0.2   # NKPC slope
    phi_pi: float = 1.5  # Taylor response to inflation
    phi_y: float = 0.5   # Taylor response to output gap
    r_star: float = 0.0  # natural real rate


def simulate_nk(T: int, shock_t: int, eps_y: float, eps_pi: float, eps_policy: float, p: NKParams):
    # Teaching-friendly lagged-expectations approximation
    y = np.zeros(T)
    pi = np.zeros(T)
    i_nom = np.zeros(T)
    for t in range(T):
        # shocks (one-time)
        uy = eps_y if t == shock_t else 0.0
        up = eps_pi if t == shock_t else 0.0
        ur = eps_policy if t == shock_t else 0.0
        # IS (gap): y_t = y_{t-1} - (1/σ)*(i_{t-1} - π_{t-1} - r*) + u^y_t
        if t == 0:
            y[t] = - (1/p.sigma) * (0 - 0 - p.r_star) + uy
        else:
            y[t] = y[t-1] - (1/p.sigma) * (i_nom[t-1] - pi[t-1] - p.r_star) + uy
        # NKPC (backward-looking teaching version): π_t = β π_{t-1} + κ y_t + u^π_t
        pi[t] = (p.beta * (0 if t==0 else pi[t-1])) + p.kappa * y[t] + up
        # Taylor rule: i_t = r* + φ_π π_t + φ_y y_t + u^i_t
        i_nom[t] = p.r_star + p.phi_pi * pi[t] + p.phi_y * y[t] + ur
    return y, pi, i_nom