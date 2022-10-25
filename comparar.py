import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('BRA1-2018-1.csv',sep=';',decimal=',')

st.write(base)

nome_busca1 = st.text_input("Nome do primeiro jogador:")

if len(base[base.Jogador==nome_busca1]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(base[base.Jogador==nome_busca1]['Jogador'])>1:
  st.write(base[base.Jogador==nome_busca1])
  clube1 = st.text_input("Clube do primeiro jogador:")
  if len(base[(base.Jogador==nome_busca1)&(base.Equipa == clube1)]['Jogador'])>1:
    st.write(base[(base.Jogador==nome_busca1)&(base.Equipa == clube1)])
    idade1 = int(st.text_input("Idade do primeiro jogador:"))
    base1 = base[(base.Jogador==nome_busca1)&(base.Equipa == clube1)&(base.Idade==idade1)]
    st.write(base1)
  else:
    base1 = base[(base.Jogador==nome_busca1)&(base.Equipa == clube1)]
    st.write(base1)
                 
else:
    base1 = base[base.Jogador == nome_busca1]
    st.write(base1)

    
nome_busca2 = st.text_input("Nome do segundo jogador:")

if len(base[base.Jogador==nome_busca2]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(base[base.Jogador==nome_busca2]['Jogador'])>1:
  st.write(base[base.Jogador==nome_busca2])
  clube2 = st.text_input("Clube do primeiro jogador:")
  if len(base[(base.Jogador==nome_busca2)&(base.Equipa == clube2)]['Jogador'])>1:
    st.write(base[(base.Jogador==nome_busca2)&(base.Equipa == clube2)])
    idade2 = int(st.text_input("Idade do primeiro jogador:"))
    base2 = base[(base.Jogador==nome_busca2)&(base.Equipa == clube2)&(base.Idade==idade2)]
    st.write(base2)
  else:
    base1 = base[(base.Jogador==nome_busca2)&(base.Equipa == clube2)]
    st.write(base2)
                 
else:
    base2 = base[base.Jogador == nome_busca2]
    st.write(base2)    
    
