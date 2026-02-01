import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.ui import header
from models.ad_as import ADASParams, ad_curve, sras_curve, lras_value

header("AD–AS Interactive Lab", "Demand and supply shocks with expectations")

col = st.sidebar
col.markdown("### AD Settings")
a = col.slider("AD intercept (a)", 50.0, 200.0, 120.0)
b = col.slider("AD slope (b)", 0.2, 2.0, 1.0, 0.05)
col.markdown("### SRAS / LRAS Settings")
y_star = col.slider("Potential output (y*)", 60.0, 160.0, 100.0)
sras_slope = col.slider("SRAS slope", 0.1, 2.0, 0.5, 0.05)
pe = col.slider("Expected price level (Pe)", 50.0, 150.0, 100.0)

P = np.linspace(50, 150, 400)
params = ADASParams(a=a, b=b, y_star=y_star, sras_slope=sras_slope, p_expected=pe)
Y_ad = ad_curve(P, params)
Y_sras = sras_curve(P, params)
Y_lras = lras_value(params)

# Intersection (approx)
idx = np.argmin(np.abs(Y_ad - Y_sras))
P_eq, Y_eq = P[idx], Y_ad[idx]

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(Y_ad, P, label="AD")
ax.plot(Y_sras, P, label="SRAS")
ax.axhline(P_eq, ls=":", lw=1)
ax.axvline(Y_eq, ls=":", lw=1)
ax.axvline(Y_lras, color="gray", lw=1, label="LRAS")
ax.scatter([Y_eq],[P_eq])
ax.set_xlabel("Output (Y)")
ax.set_ylabel("Price level (P)")
ax.legend()
st.pyplot(fig)

st.metric("Equilibrium Y", f"{Y_eq:.1f}")
st.metric("Equilibrium P", f"{P_eq:.1f}")

st.caption("Shift AD via a,b (demand); SRAS via Pe and slope; LRAS via y*.")