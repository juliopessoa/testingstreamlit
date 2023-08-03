import streamlit as st
import pandas as pd
import requests
from io import StringIO

# URL do dataset
url = "https://dadosabertos.ans.gov.br/FTP/PDA/caracteristicas_produtos_saude_suplementar/caracteristicas_produtos_saude_suplementar.csv"

# Fazendo o download do dataset
@st.cache
def load_data():
    response = requests.get(url)
    data = response.content.decode('utf-8')
    df = pd.read_csv(StringIO(data), sep=';')
    return df

# Carregando os dados
df = load_data()

# Título do painel
st.title("Painel de Visualização de Dados de Planos de Saúde")

# Exibindo os dados em formato de tabela
st.write(df)
