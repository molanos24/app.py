import streamlit as st

def balance_combustion(fuel_type, carbon, hydrogen):
    oxygen_needed = (carbon * 2 + hydrogen / 2) / 2
    return f"C{carbon}H{hydrogen} + {oxygen_needed} O2 -> {carbon} CO2 + {hydrogen // 2} H2O"

st.title("Balanceador de Reacciones de Combustión")

fuel_type = st.selectbox("Selecciona el tipo de hidrocarburo:", ["Alcano", "Alqueno", "Alquino"])
carbon = st.number_input("Número de átomos de Carbono (C):", min_value=1, step=1)
hydrogen = st.number_input("Número de átomos de Hidrógeno (H):", min_value=2, step=2)

if st.button("Balancear Reacción"):
    reaction = balance_combustion(fuel_type, carbon, hydrogen)
    st.write("Reacción balanceada:")
    st.latex(reaction)
