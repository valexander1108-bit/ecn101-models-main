# models/is_lm.py — Minimal IS–LM with numerical intersection
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ISLMParams:
    c0: float = 50.0     # autonomous consumption
    c1: float = 0.6      # MPC
    i0: float = 40.0     # autonomous investment
    i1: float = 20.0     # interest sensitivity of investment
    g: float = 100.0     # government spending
    t: float = 0.2       # tax rate
    m: float = 300.0     # real money supply (M/P)
    k: float = 0.5       # money demand sensitivity to income
    h: float = 40.0      # money demand sensitivity to interest

def is_curve(params: ISLMParams, r_grid: np.ndarray):
    """
    Goods market (Keynesian cross collapsed into IS line):
    Y = A + c1(1-t)Y - i1 r  => Y(1 - c1(1-t)) = A - i1 r
    """
    A = params.c0 + params.i0 + params.g
    denom = (1 - params.c1 * (1 - params.t))
    slope = -params.i1 / denom
    intercept = A / denom
    Y = intercept + slope * r_grid
    return Y

def lm_curve(params: ISLMParams, r_grid: np.ndarray):
    """
    Money market:
    M/P = kY - h r  => Y = (M/P + h r)/k
    """
    Y = (params.m + params.h * r_grid) / params.k
    return Y

def solve_equilibrium(params: ISLMParams):
    r = np.linspace(0, 20, 400)
    Y_is = is_curve(params, r)
    Y_lm = lm_curve(params, r)
    idx = np.argmin(np.abs(Y_is - Y_lm))
    return r[idx], Y_is[idx], (r, Y_is, Y_lm)