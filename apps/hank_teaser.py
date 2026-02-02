import streamlit as st
import matplotlib.pyplot as plt
from models.hank_teaser import HANKTeaserParams, simulate_hank


def app():
    st.subheader("HANK Teaser: Heterogeneity & Policy Transmission")
    st.caption("Two-type households: Hand-to-Mouth vs Savers")

    cols = st.columns(5)
    with cols[0]:
        lam = st.slider("Share HtM (λ)", 0.0, 1.0, 0.4, 0.05)
    with cols[1]:
        mpc_h = st.slider("MPC HtM", 0.2, 1.0, 0.9, 0.05)
    with cols[2]:
        mpc_s = st.slider("MPC Saver", 0.0, 0.8, 0.3, 0.05)
    with cols[3]:
        ir_el = st.slider("Saver i-elasticity", -1.5, 0.0, -0.5, 0.05)
    with cols[4]:
        mult = st.slider("Demand multiplier", 0.5, 3.0, 1.2, 0.1)

    T = st.slider("Horizon", 10, 80, 40)
    shock_t = st.slider("Shock timing", 0, 10, 1)
    inc = st.slider("Transitory income shock (ΔY %)", -5.0, 5.0, -2.0, 0.1)
    rate = st.slider("Policy rate shock (pp)", -2.0, 2.0, 1.0, 0.1)

    params = HANKTeaserParams(
        lam_htm=lam,
        mpc_htm=mpc_h,
        mpc_saver=mpc_s,
        ir_elast_saver=ir_el,
        multiplier=mult,
    )
    dC_h, dC_s, dC, dY = simulate_hank(T, shock_t, inc, rate, params)

    for series, title, ylabel in [
        (dC_h, "HtM Consumption ΔC%", "%"),
        (dC_s, "Saver Consumption ΔC%", "%"),
        (dC, "Aggregate Consumption ΔC%", "%"),
        (dY, "Output ΔY% (index)", "%"),
    ]:
        fig, ax = plt.subplots(figsize=(5, 2.6))
        ax.plot(series)
        ax.axhline(0, color="gray", lw=1, ls=":")
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel("t")
        st.pyplot(fig)

    st.markdown(
        "**Takeaway:** Higher λ (more HtM) → stronger income-driven transmission; "
        "stronger saver interest elasticity → bigger response to rate cuts/raises. "
        "This is the core idea behind HANK relative to representative-agent NK."
    )
