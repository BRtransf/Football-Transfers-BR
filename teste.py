import streamlit as st
import pandas as pd

base = pd.read_excel('https://github.com/BRtransf/Football-Transfers-BR/blob/main/base1.xlsx').append(pd.read_excel('https://github.com/BRtransf/Football-Transfers-BR/blob/main/base1.xlsx')).drop_duplicates()

st.write(base)
