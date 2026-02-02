import numpy as np
from dataclasses import dataclass

@dataclass
class HANKTeaserParams:
    lam_htm: float = 0.4       # share of hand-to-mouth households
    mpc_htm: float = 0.9       # MPC of HtM
    mpc_saver: float = 0.3     # MPC of Ricardian savers (out of transitory income)
    ir_elast_saver: float = -0.5  # dC/C per 1pp rise in i (savers)
    multiplier: float = 1.2    # demand multiplier to map ΔC -> ΔY
    shock_decay: float = 0.7   # AR(1) decay for shocks


def simulate_hank(T: int, t_shock: int, dY_transitory: float, dI_pp: float, p: HANKTeaserParams):
    """
    Teaching-only reduced-form dynamics:
    - HtM consumption reacts strongly to transitory income; little direct rate sensitivity
    - Saver consumption reacts to income (lower MPC) and to interest rate (intertemporal substitution)
    - Aggregate ΔC_t = λ·ΔC_HtM + (1-λ)·ΔC_Saver; ΔY_t = multiplier·ΔC_t
    """
    shock = np.zeros(T)
    if 0 <= t_shock < T:
        shock[t_shock] = dY_transitory
    # AR(1) process for income shock
    for t in range(1, T):
        shock[t] += p.shock_decay * shock[t-1]

    dC_htm = p.mpc_htm * shock  # HtM respond to income
    # Savers: income + interest-rate channel
    dC_saver = p.mpc_saver * shock + (p.ir_elast_saver * dI_pp) * np.exp(-0.2*np.arange(T))

    dC = p.lam_htm * dC_htm + (1 - p.lam_htm) * dC_saver
    dY = p.multiplier * dC
    return dC_htm, dC_saver, dC, dY