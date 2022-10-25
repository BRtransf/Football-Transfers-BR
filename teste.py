import streamlit as st
import pandas as pd

base = pd.read_excel('base1.xlsx')

st.write(base)
