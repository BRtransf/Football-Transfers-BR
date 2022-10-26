import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



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

base1 = base1.assign(ID = 1)    

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

base2 = base2.assign(ID = 2)       

ano1min = int(np.nanmin(base1.Ano))
ano1max = int(np.nanmax(base1.Ano))
ano2min = int(np.nanmin(base2.Ano))
ano2max = int(np.nanmax(base2.Ano))

if ano1min < ano1max:
  anos1 = st.slider('Anos analisados para Jogador 1',ano1min, ano1max, (ano1min, ano1max))
  st.write('Values:', anos1)
else:
  st.write("Jogador 1 somente disponível em "+str(ano1min))
  anos1 = [ano1min,ano1max]

if ano2min < ano2max:
  anos2 = st.slider('Anos analisados para Jogador 2',ano2min, ano2max, (ano2min, ano2max))
  st.write('Values:', anos2)
else:
  st.write("Jogador 2 somente disponível em "+str(ano2min))
  anos2 = [ano2min,ano2max]

df = pd.concat([base1[(base1.Ano>=anos1[0])&(base1.Ano<=anos1[1])],base2[(base2.Ano>=anos2[0])&(base2.Ano<=anos2[1])]])

vars = st.multiselect(label = 'Variáveis de comparação',options=df.columns[7:])
lista_vars = ['Jogador','Equipe atual','Equipe no ano','Posição','Idade']
for var in vars:
  lista_vars.append(str(var))

st.write(lista_vars)
df_comp = df[lista_vars].copy()

st.write(df_comp)



fig = plt.figure(figsize = (8,8), tight_layout=True, facecolor='aliceblue')

gs = fig.add_gridspec(5,4)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1:])
ax3 = fig.add_subplot(gs[1:5, 0:4],polar = True)


lista_axs = [ax3]

ax1.axis("off")

ax2.annotate(xy = (0, .5),
    text = 'Comparação: '+ pd.unique(df_comp.Jogador.tolist())[0]+' X '+pd.unique(df_comp.Jogador.tolist())[1],
    ha = "left",
    va = "center",
    weight = "bold",
    size = 20,
    color='royalblue')
ax2.axis("off")

v = 0

for jogador in pd.unique(df_comp.Jogador):
    
    aux_df = df_comp[df_comp.Jogador == jogador].loc[:, df_comp.columns != 'Jogador']
    aux_df = aux_df.loc[:, aux_df.columns != 'Equipe atual']
    aux_df = aux_df.loc[:, aux_df.columns != 'Equipe no ano']
    aux_df = aux_df.loc[:, aux_df.columns != 'Posição']
    aux_df = aux_df.loc[:, aux_df.columns != 'Idade']
    
    aux_df = aux_df.reset_index(drop=True)
    
    categories = aux_df.columns.tolist()
    categories.append(categories[0])
    
    r = aux_df[0:1].values.tolist()
    lista_raio = []
    for item in r:
        t = 0
        while t < len(item):
            lista_raio.append(item[t])
            t += 1
    
    lista_raio.append(lista_raio[0])
    
    
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(lista_raio))
    
    lista_axs[v].plot(label_loc,lista_raio, label=jogador,marker='.')
        
    lista_axs[v].set_thetagrids(np.degrees(label_loc), labels=categories)
    
    lista_axs[v].set_facecolor('aliceblue')
    
    lista_axs[v].set_rticks([0,1,2,3,4,5,6])
    
    lista_axs[v].set_ylim(0,7)
    
    lista_axs[v].fill(label_loc,lista_raio,alpha=0.2)
    
    lista_axs[v].legend()

st.pyplot(fig)

''' está aparecendo só a primeira linha de cada jogador, precisa somar'''
