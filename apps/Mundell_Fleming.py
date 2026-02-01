import streamlit as st
from utils.ui import header
from models.mundell_fleming import MFParams

header("Mundell–Fleming (Open Economy)", "Policy trilemma: capital mobility, exchange regime, autonomy")

k = st.slider("Capital mobility", 0.0, 1.0, 0.8, 0.05)
e_fixed = st.toggle("Fixed exchange rate", value=False)

st.markdown("""
**Rules of thumb**
- With **high mobility** & **fixed FX**, monetary policy is weak; fiscal is stronger.
- With **floating FX**, monetary policy is powerful; fiscal may be dampened by crowding out via exchange rate.
- The **trilemma**: you cannot simultaneously have fixed FX, free capital, and monetary autonomy.
""")

st.info("Extension: add simple algebraic curves (IS–LM–BP) in Y–i space and show shifts across regimes.")