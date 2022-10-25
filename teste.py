import streamlit as st
import pandas as pd

base = pd.read_csv('base1.csv',sep=';').append(pd.read_csv('base2.csv',sep=';')).drop_duplicates()

st.write(len(base))
