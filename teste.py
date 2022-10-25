import streamlit as st
import pandas as pd

base = pd.concat(pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')).drop_duplicates(subset=['Jogador','Equipa'])

st.write(len(base))
