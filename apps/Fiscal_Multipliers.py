import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def app():
    st.subheader("Fiscal Sandbox: Multipliers & Debt Dynamics")
    st.caption("When does stimulus help, and what happens to debt?")

    mult = st.slider("Fiscal multiplier", 0.0, 3.0, 1.2, 0.1)
    shock_g = st.slider("ΔG (as % of Y)", -5.0, 5.0, 2.0, 0.1)

    Y0 = 100.0
    Y1 = Y0 * (1 + (mult * shock_g) / 100)
    st.metric("Output after shock (index)", f"{Y1:.2f}")

    st.subheader("Debt dynamics (stylized)")
    d0 = st.slider("Debt/GDP start (%)", 0.0, 200.0, 90.0, 1.0)
    i = st.slider("Nominal interest (%)", 0.0, 10.0, 3.0, 0.1)
    g = st.slider("Nominal GDP growth (%)", -5.0, 10.0, 4.0, 0.1)
    primary = st.slider("Primary balance (% of GDP; +surplus / -deficit)", -10.0, 10.0, -3.0, 0.5)
    T = st.slider("Years", 1, 50, 20)

    D = np.zeros(T)
    D[0] = d0
    for t in range(1, T):
        D[t] = ((1 + i / 100) / (1 + g / 100)) * D[t - 1] - primary

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(D)
    ax.set_xlabel("Years")
    ax.set_ylabel("Debt/GDP (%)")
    st.pyplot(fig)

    st.caption("Basic arithmetic of debt dynamics. Explore r−g gap and primary balances.")
