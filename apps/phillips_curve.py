import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from models.phillips import NKPCParams, nkpc_next


def app():
    st.subheader("Phillips Curve (NKPC, teaching form)")
    st.caption("Inflation dynamics from output gaps and shocks")

    col1, col2 = st.columns(2)
    with col1:
        beta = st.slider("β (inflation persistence)", 0.0, 0.99, 0.9, 0.01)
        kappa = st.slider("κ (slope)", 0.0, 1.0, 0.2, 0.01)
    with col2:
        T = st.slider("Horizon (T)", 5, 80, 30)
        shock_t = st.slider("Shock timing", 0, 20, 3)

    y_gap = st.slider("Output gap (y~)", -4.0, 4.0, 1.0, 0.1)
    u = st.slider("Cost-push shock (u)", -3.0, 3.0, 0.5, 0.1)
    decay = st.slider("Shock decay (AR)", 0.0, 0.95, 0.6, 0.05)

    params = NKPCParams(beta=beta, kappa=kappa)
    shocks = np.zeros(T)
    if 0 <= shock_t < T:
        shocks[shock_t] = u
    for t in range(1, T):
        shocks[t] += decay * shocks[t - 1]

    pi = np.zeros(T)
    for t in range(1, T):
        pi[t] = nkpc_next(pi[t - 1], y_gap, shocks[t], params)

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(pi, label="Inflation (π)")
    ax.axhline(0, color="gray", lw=1, ls=":")
    ax.set_xlabel("t")
    ax.set_ylabel("π")
    ax.legend()
    st.pyplot(fig)

    st.metric("Inflation (last period)", f"{pi[-1]:.2f}")
    st.caption("Set y~ > 0 to see inflation drift up; shocks add temporary spikes that decay.")
