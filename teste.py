import streamlit as st
import pandas as pd

data_url = ("https://github.com//BRtransf/Football-Transfers-BR/blob/main/base1.xlsx?raw=true")

base = pd.read_excel(data_url)

st.write(base)
