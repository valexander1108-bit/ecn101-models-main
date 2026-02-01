# --- NAV & ROUTER (replace your current block with this) ---
import importlib.util
from pathlib import Path
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
    "Module 6 — Core Macro Models": [
        "IS–LM",
        "AD–AS",
        "Solow Model",
    ],
    "Module 7 — Extension Macro Models": [
        "NK DSGE",
        "Mundell–Fleming",
        "Fiscal Multipliers",
        "HANK",
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

def run_app_from_file(rel_path, module_name, label):
    file_path = Path(__file__).resolve().parent / rel_path
    if not file_path.exists():
        st.error(f"{label} file not found: {rel_path}")
        return
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        st.error(f"Unable to load {label} module from {rel_path}")
        return
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "app"):
        mod.app()
    else:
        st.error(f"{label} module is missing an app() entry point.")

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
elif page == "Surplus":
    from apps.surplus import app as sur_app; sur_app()
elif page == "Government Intervention: Price Floor":
    from apps.gov_int_p_floor import app as floor_app; floor_app()
elif page == "Government Intervention: Price Ceiling":
    from apps.gov_int_p_ceiling import app as ceiling_app; ceiling_app()
elif page == "Deadweight Loss":
    from apps.deadweight_loss import app as dw_app; dw_app()
elif page == "Interdependent Factors":
    from apps.all_factors import app as fact_app; fact_app()
elif page == "Land + Rent":
    from apps.land import app as lan_app; lan_app()
elif page == "Labor + Wage":
    from apps.labor import app as lab_app; lab_app()
elif page == "Capital + Interest":
    from apps.capital import app as cap_app; cap_app()
elif page == "IS–LM":
    run_app_from_file("apps/IS-LM.py", "apps.is_lm_file", "IS–LM")
elif page == "AD–AS":
    run_app_from_file("apps/ad_as.py", "apps.ad_as", "AD–AS")
elif page == "Solow Model":
    run_app_from_file("apps/solow_model.py", "apps.solow_model", "Solow Model")
elif page == "NK DSGE":
    run_app_from_file("apps/nk_dsge", "apps.nk_dsge_file", "NK DSGE")
elif page == "Mundell–Fleming":
    run_app_from_file("apps/Mundell_Fleming.py", "apps.mundell_fleming_file", "Mundell–Fleming")
elif page == "Fiscal Multipliers":
    run_app_from_file("apps/Fiscal_Multipliers.py", "apps.fiscal_multipliers_file", "Fiscal Multipliers")
elif page == "HANK":
    run_app_from_file("apps/hank_teaser.py", "apps.hank_teaser", "HANK")
