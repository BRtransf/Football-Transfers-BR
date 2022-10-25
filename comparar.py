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
    df['Ano'] = int(ano)
    base = base.append(df).drop_duplicates().reset_index(drop=True)

base = base.rename(columns={"Equipa dentro de um período de tempo seleccionado":"Equipe no ano","Equipa":"Equipe atual"})
    
st.write(base[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])

st.subheader('Jogador 1')
nome_busca1 = st.text_input("Nome do primeiro jogador:")

if len(base[base.Jogador==nome_busca1]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(pd.unique(base[base.Jogador==nome_busca1]['Equipe atual']))>1:
  st.write(base[base.Jogador==nome_busca1])
  clube1 = st.text_input("Clube do primeiro jogador:")
  if len(pd.unique(base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)]['Idade']))>1:
    st.write(base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)])
    idade1 = int(st.text_input("Idade do primeiro jogador:"))
    base1 = base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)&(base.Idade==idade1)]
    st.write(base1)
  else:
    base1 = base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)]
    st.write(base1)
                 
else:
    base1 = base[base.Jogador == nome_busca1]
    st.write(base1)

st.subheader('Jogador 2')    
nome_busca2 = st.text_input("Nome do segundo jogador:")

if len(base[base.Jogador==nome_busca2]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(pd.unique(base[base.Jogador==nome_busca2]['Equipe atual']))>1:
  st.write(base[base.Jogador==nome_busca2])
  clube2 = st.text_input("Clube do segundo jogador:")
  if len(pd.unique(base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)]['Idade']))>1:
    st.write(base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)])
    idade2 = int(st.text_input("Idade do segundo jogador:"))
    base2 = base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)&(base.Idade==idade2)]
    st.write(base2)
  else:
    base2 = base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)]
    st.write(base2)
                 
else:
    base2 = base[base.Jogador == nome_busca2]
    st.write(base2)    
    
ano1min = int(np.nanmin(base1.Ano))
ano1max = int(np.nanmax(base1.Ano))
ano2min = int(np.nanmin(base2.Ano))
ano2max = int(np.nanmax(base2.Ano))

anos1 = st.slider('Anos analisados para Jogador 1',ano1min, ano1max, (ano1min, ano1max))
st.write('Values:', anos1)

anos2 = st.slider('Anos analisados para Jogador 2',ano2min, ano2max, (ano2min, ano2max))
st.write('Values:', anos2)


df = pd.concat([base1[(base1.Ano>ano1min)&(base1.Ano<ano1max)],base2[(base2.Ano>ano2min)&(base2.Ano<ano2max)]])

vars = st.multiselect(label = 'Variáveis de comparação',options=df.columns)
