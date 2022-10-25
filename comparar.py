import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('BRA1-2018-1.csv',sep=';',decimal=',')

st.write(base)

nome_busca1 = st.input_text("Nome do primeiro jogador:")

if len(base[base.Jogador==nome_busca1]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout)")

elif len(base[base.Jogador==nome_busca1]['Jogador'])>1:
  st.write(base[base.Jogador==nome_busca1])
  clube1 = st.input_text("Clube do primeiro jogador:")
  if len(base[(base.Jogador==nome_busca1)&(base.Equipa == clube1)]['Jogador'])>1:
    st.write(base[(base.Jogador==nome_busca1)&(base.Equipa == clube)])
    idade1 = int(st.input_text("Idade do primeiro jogador:")
    st.write("Jogador selecionado: "+ nome_busca1+ clube1+str(idade1))
                 
else:
    idade1 = base[base.Jogador==nome_busca1]['Idade'].tolist()[0]
    clube1 = base[base.Jogador==nome_busca1]['Equipa'].tolist()[0]
    st.write("Jogador selecionado: "+ nome_busca1+ clube1+str(idade1))
