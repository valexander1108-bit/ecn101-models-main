from dataclasses import dataclass

@dataclass
class MFParams:
    k: float = 0.5   # capital mobility (0 low → 1 high)
    e_fixed: bool = False  # fixed exchange rate regime
