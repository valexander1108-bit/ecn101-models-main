import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from models.is_lm import ISLMParams, solve_equilibrium, is_curve, lm_curve


def app():
    st.subheader("IS–LM Interactive Lab")
    st.caption("Short-run stabilization and demand/monetary shocks")

    # Sidebar controls
    with st.sidebar:
        st.markdown("### IS Parameters (Goods Market)")
        c0 = st.slider("Autonomous consumption (c0)", 0.0, 200.0, 50.0)
        c1 = st.slider("MPC (c1)", 0.0, 0.95, 0.60, 0.01)
        i0 = st.slider("Autonomous investment (i0)", 0.0, 200.0, 40.0)
        i1 = st.slider("Interest sensitivity of I (i1)", 0.0, 60.0, 20.0)
        g = st.slider("Government spending (g)", 0.0, 400.0, 100.0)
        t = st.slider("Tax rate (t)", 0.00, 0.60, 0.20, 0.01)

        st.markdown("### LM Parameters (Money Market)")
        m = st.slider("Real money supply (M/P)", 50.0, 1000.0, 300.0)
        k = st.slider("Money demand sensitivity to Y (k)", 0.10, 2.00, 0.50, 0.01)
        h = st.slider("Money demand sensitivity to r (h)", 1.0, 100.0, 40.0)

    # Build params & solve
    params = ISLMParams(c0=c0, c1=c1, i0=i0, i1=i1, g=g, t=t, m=m, k=k, h=h)
    r_star, Y_star, (r_grid, Y_is, Y_lm) = solve_equilibrium(params)

    # Plot curves and equilibrium
    col1, col2 = st.columns([2, 1])
    with col1:
        fig, ax = plt.subplots(figsize=(6.5, 4))
        ax.plot(r_grid, Y_is, label="IS")
        ax.plot(r_grid, Y_lm, label="LM")
        ax.scatter([r_star], [Y_star])
        ax.set_xlabel("Interest rate (r)")
        ax.set_ylabel("Income / Output (Y)")
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.metric("Equilibrium interest rate r*", f"{r_star:.2f}")
        st.metric("Equilibrium output Y*", f"{Y_star:.1f}")
        st.markdown("**Shock tips**")
        st.caption(
            "- ↑g or ↓t → IS shifts right\n"
            "- ↑M/P → LM shifts right\n"
            "- ↑h (rate-sensitivity of money demand) → LM flatter\n"
            "- ↑i1 (rate-sensitivity of investment) → IS flatter"
        )

    st.markdown("**Discussion:** How would adding expectations (intertemporal IS) alter the slope/position of IS?")
