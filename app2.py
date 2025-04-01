import streamlit as st
from sympy import symbols, Eq, solve

def balance_combustion(fuel_type, carbon, hydrogen):
    CxHy = symbols('CxHy')
    O2 = symbols('O2')
    CO2 = symbols('CO2')
    H2O = symbols('H2O')
    
    eq1 = Eq(carbon, CO2)
    eq2 = Eq(hydrogen, 2 * H2O)
    eq3 = Eq(2 * O2, 2 * CO2 + H2O)
    
    sol = solve((eq1, eq2, eq3), (CO2, H2O, O2))
    
    return f"{fuel_type} + {sol[O2]} O2 -> {sol[CO2]} CO2 + {sol[H2O]} H2O"

st.title("Balanceador de Reacciones de Combustión")

fuel_type = st.selectbox("Selecciona el tipo de hidrocarburo:", ["Alcano", "Alqueno", "Alquino"])
carbon = st.number_input("Número de átomos de Carbono (C):", min_value=1, step=1)
hydrogen = st.number_input("Número de átomos de Hidrógeno (H):", min_value=2, step=2)

if st.button("Balancear Reacción"):
    reaction = balance_combustion(fuel_type, carbon, hydrogen)
    st.write("Reacción balanceada:")
    st.latex(reaction)
