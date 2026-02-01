# pages/6_🌱_Solow_Lab.py — Solow Growth Lab
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.ui import header
from models.solow import SolowParams, simulate_path

header("Solow Growth Lab", "Steady state and convergence dynamics")

# Controls
with st.sidebar:
    st.markdown("### Parameters")
    s = st.slider("Savings rate (s)", 0.00, 0.80, 0.20, 0.01)
    alpha = st.slider("Capital share (α)", 0.10, 0.60, 0.33, 0.01)
    delta = st.slider("Depreciation (δ)", 0.00, 0.20, 0.05, 0.005)
    n = st.slider("Population growth (n)", -0.02, 0.05, 0.01, 0.001)
    g = st.slider("Technology growth (g)", -0.02, 0.08, 0.02, 0.001)

    st.markdown("### Simulation")
    k0 = st.slider("Initial capital per effective worker (k₀)", 0.01, 10.0, 2.0, 0.01)
    T = st.slider("Horizon (periods)", 10, 300, 120)

params = SolowParams(s=s, delta=delta, n=n, g=g, alpha=alpha)
k, y = simulate_path(k0=k0, T=T, params=params)

# Plots
c1, c2 = st.columns(2)

with c1:
    fig1, ax1 = plt.subplots(figsize=(6, 3.6))
    ax1.plot(k, label="k_t")
    ax1.set_xlabel("t")
    ax1.set_ylabel("Capital per effective worker (k)")
    ax1.legend()
    st.pyplot(fig1)

with c2:
    fig2, ax2 = plt.subplots(figsize=(6, 3.6))
    ax2.plot(y, label="y_t = k_t^α")
    ax2.set_xlabel("t")
    ax2.set_ylabel("Output per effective worker (y)")
    ax2.legend()
    st.pyplot(fig2)

# Simple steady-state hint (not closed-form here; show last values)
st.metric("k (last period)", f"{k[-1]:.3f}")
st.metric("y (last period)", f"{y[-1]:.3f}")
st.caption("Observe convergence toward a steady state driven by s, α, δ and diluted by n+g.")

st.markdown("**Questions:** What happens to steady state if s↑? If δ↑? How does (n+g) change the speed of convergence?")
