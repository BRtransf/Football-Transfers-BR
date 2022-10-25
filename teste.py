import streamlit as st
import pandas as pd

base = pd.read_csv('base1.csv',sep=';')

st.write(base)
