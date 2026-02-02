import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from models.solow import SolowParams, simulate_path


def app():
    st.subheader("Solow Growth Lab")
    st.caption("Steady state and convergence dynamics")

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
    ngd = params.n + params.g + params.delta
    k_star = None
    if ngd > 0:
        k_star = (params.s / ngd) ** (1 / (1 - params.alpha))
        y_star = k_star ** params.alpha
    else:
        y_star = None

    with c1:
        fig1, ax1 = plt.subplots(figsize=(6, 3.6))
        ax1.plot(k, label="k_t")
        if k_star is not None:
            ax1.axhline(k_star, color="gray", lw=1, ls=":")
            ax1.text(0.02, 0.95, "k* steady state", transform=ax1.transAxes, va="top")
        ax1.set_xlabel("t")
        ax1.set_ylabel("Capital per effective worker (k)")
        ax1.legend()
        st.pyplot(fig1)

    with c2:
        fig2, ax2 = plt.subplots(figsize=(6, 3.6))
        ax2.plot(y, label="y_t = k_t^α")
        if y_star is not None:
            ax2.axhline(y_star, color="gray", lw=1, ls=":")
            ax2.text(0.02, 0.95, "y* steady state", transform=ax2.transAxes, va="top")
        ax2.set_xlabel("t")
        ax2.set_ylabel("Output per effective worker (y)")
        ax2.legend()
        st.pyplot(fig2)

    if k_star is not None:
        st.metric("k* (steady state)", f"{k_star:.3f}")
        st.metric("y* (steady state)", f"{y_star:.3f}")
    else:
        st.warning("Steady state undefined when n + g + δ ≤ 0.")

    st.metric("k (last period)", f"{k[-1]:.3f}")
    st.metric("y (last period)", f"{y[-1]:.3f}")
    st.caption("Higher s shifts k* upward; higher (n+g+δ) shifts k* downward.")

    # Savings vs. break-even investment diagram
    st.subheader("Savings vs. Break-Even Investment")
    k_grid = np.linspace(0.01, max(5.0, k_star * 1.2 if k_star else 10.0), 300)
    s_f = params.s * (k_grid ** params.alpha)
    breakeven = ngd * k_grid
    fig3, ax3 = plt.subplots(figsize=(6, 3.6))
    ax3.plot(k_grid, s_f, label="s·f(k)")
    ax3.plot(k_grid, breakeven, label="(n+g+δ)·k")
    if k_star is not None:
        ax3.scatter([k_star], [params.s * (k_star ** params.alpha)], zorder=3)
        ax3.text(k_star, params.s * (k_star ** params.alpha), "  k*", va="bottom")
    ax3.set_xlabel("k")
    ax3.set_ylabel("Investment per effective worker")
    ax3.legend()
    st.pyplot(fig3)

    st.markdown("**Questions:** What happens to steady state if s↑? If δ↑? How does (n+g) change the speed of convergence?")
