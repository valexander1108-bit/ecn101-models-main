# --- NAV & ROUTER (replace your current block with this) ---
import streamlit as st

options = [
    "Budget Constraint","PPC","Comparative Advantage",
    "Demand (schedule → line)","Supply (schedule → line)",
    "Static Equilibrium","Shifts (single)","Shifts (double)",
    "Price Elasticity of Demand","Elasticity and Total Revenue","Price Elasticity of Supply", 
    "Surplus","Government Intervention: Price Floor","Government Intervention: Price Ceiling",
    "Deadweight Loss", "Interdependent Factors", "Land + Rent",
    "Labor + Wage","Capital + Interest", 
]
import streamlit as st

MODULES = {
    "Module 1 — Modeling Foundations": [
        "Budget Constraint",
        "PPC",
        "Comparative Advantage",
    ],
    "Module 2 — Supply & Demand": [
        "Demand (schedule → line)",
        "Supply (schedule → line)",
        "Market Model",
        "Single Shifts",
        "Double Shifts",
    ],
    "Module 3 — Elasticity": [
        "Price Elasticity of Demand",
        "Elasticity and Total Revenue",
        "Price Elasticity of Supply",
    ],
    "Module 4 — Welfare Economics": [
        "Surplus",
        "Government Intervention: Price Floor", 
        "Government Intervention: Price Ceiling",
        "Deadweight Loss"
    ],
     "Module 5 — Factors of Production": [
        "Interdependent Factors",
        "Land + Rent", 
        "Labor + Wage",
        "Capital + Interest"
    ],
}
# flat list if you ever need it
ALL_PAGES = [p for pages in MODULES.values() for p in pages]

# read “default target” set by subpages (if any)
default = st.session_state.get("nav_default", options[0])

# read default target set by subpages (string page name), fallback to first page
default_page = st.session_state.get("nav_default", ALL_PAGES[0])

# find the default module containing that page
def find_module_for(page):
    for mod, pages in MODULES.items():
        if page in pages:
            return mod
    return list(MODULES.keys())[0]

default_module = find_module_for(default_page)

with st.sidebar:
    st.header("Navigate")
    module = st.selectbox("Module", list(MODULES.keys()),
                          index=list(MODULES.keys()).index(default_module),
                          key="module_select")
    page = st.selectbox("Page", MODULES[module],
                        index=MODULES[module].index(default_page) if default_page in MODULES[module] else 0,
                        key="page_select")

# consume the default so it doesn't keep forcing selection
st.session_state.pop("nav_default", None)

# consume the default so it doesn't stick
st.session_state.pop("nav_default", None)

if page == "Budget Constraint":
    from apps.budget_line import app as budget_app; budget_app()
elif page == "PPC":
    from apps.ppc import app as ppc_app; ppc_app()
elif page == "Comparative Advantage":
    from apps.comparative_advantage import app as ca_app; ca_app()
elif page == "Demand (schedule → line)":
    from apps.demand_schedule import app as dem_app; dem_app()
elif page == "Supply (schedule → line)":
    from apps.supply_schedule import app as sup_app; sup_app()
elif page == "Market Model":
    from apps.static_equilibrium import app as se_app; se_app()
elif page == "Single Shifts":
    from apps.shifts_single import app as ss_app; ss_app()
elif page == "Double Shifts":
    from apps.shifts_double import app as sd_app; sd_app()
elif page == "Price Elasticity of Demand":
    from apps.elasticity_demand import app as ed_app; ed_app()
elif page == "Elasticity and Total Revenue":
    from apps.elasticity_tr import app as etr_app; etr_app()
elif page == "Price Elasticity of Supply":
    from apps.elasticity_supply import app as es_app; es_app()
elif page == "Surlpus":
    from apps.surplus import app as sur_app; sur_app()
elif page == "Government Intervention: Price Floor":
    from apps.gov_int_p_floor import app as floor_app; floor_app()
elif page == "Government Intervention: Price Ceiling":
    from apps.gov_int_p_ceiling import app as ceiling_app; ceiling_app()
elif page == "Deadweight Loss":
    from apps.deadweight import app as dw_app; dw_app()
elif page == "Interdependent Factors":
    from apps.all_factors import app as fact_app; fact_app()
elif page == "Land + Rent":
    from apps.land import app as lan_app; lan_app()
elif page == "Labor + Wage":
    from apps.labor import app as lab_app; lab_app()
elif page == "Capital + Interest":
    from apps.capital import app as cap_app; cap_app()