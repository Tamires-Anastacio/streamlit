import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#configuração da página

st.set_page_config(
    page_title="Minha página",
    page_icon= "img/icon.png",
    layout="wide"
)

st.markdown("# 🪶 Minha Pagina 1 - texto corpo")

st.sidebar.markdown("Meu site 01 - texto menu")

#-------------------------------------------------------------
#imagem
st.header("Exibindo imagem")
st.image("img/01.jpg", caption="Minha foto", width=500)
#----------------------------------------------------------------

#Vídeo
st.header('Exibindo vídeo')
st.video("video/trailer.mp4", width=500)
# -------------------------------

#Áudio
st.header('Exibindo áudio')
st.audio("audio/house_lo.mp3", width=500)

#----------------------------------------------------
# edicao de tabelas usando Pandas
data = {
    'Nome':['João', 'Pedro', 'Tiago', 'Alicia'],
    'Idade':[16, 15, 22, 18],
    'Salario':[5000, 4500, 6000, 5800],
    'Altura':[1.70, 1.65, 1.80, 1.75]
}

df = pd.DataFrame(data)
st.dataframe(df) # tabela interativa
st.table(df)  #tabela simplificada




