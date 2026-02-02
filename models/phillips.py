from dataclasses import dataclass

@dataclass
class NKPCParams:
    beta: float = 0.9
    kappa: float = 0.2


def nkpc_next(pi_prev: float, y_gap: float, u_t: float, p: NKPCParams) -> float:
    # π_t = β π_{t-1} + κ y_t + u_t (teaching form)
    return p.beta * pi_prev + p.kappa * y_gap + u_t