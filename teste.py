import streamlit as st
import pandas as pd

base = pd.read_excel('base1.xlsx').append(pd.read_excel('base2.xlsx')).drop_duplicates()

st.write(base)
