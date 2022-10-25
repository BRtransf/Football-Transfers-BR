import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('BRA1-2018-1.csv',sep=';',decimal=',')

st.write(base)
