import streamlit as st
import pandas as pd
import numpy as np


lista_anos = []
for ano in range(2018,2022):
  lista_anos.append(str(ano))

base = pd.DataFrame() 

for ano in lista_anos:
  for item in range(1,3):
    arquivo = 'BRA1-'+ano+'-'+str(item)+'.csv'
    df = pd.read_csv(arquivo,sep=';',decimal=',')
    df['Ano'] = ano
    base = base.append(df).drop_duplicates().reset_index(drop=True)

st.write(base[['Jogador','Equipa','Minutos jogados:','Ano']])

st.subheader('Jogador 1')
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

st.subheader('Jogador 2')    
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
    
