import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("#Minha pagina 2 -- texto corpo")

st.sidebar.markdown("Meu site 02 -- texto menu")

st.header("Hello people!!")

opcao = st.selectbox(
    'Escolha um departamento:',
    ['RH', 'T.I', 'Vendas', 'Marketing']
)

st.write(f"Departamento selecionado: {opcao}")