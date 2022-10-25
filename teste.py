import streamlit as st
import pandas as pd
import numpy as np
from shapely.geometry import Polygon
from matplotlib import pyplot as plt

base = pd.concat([pd.read_csv('base1.csv',sep=';',decimal=','),pd.read_csv('base2.csv',sep=';',decimal=',')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

      
st.write(len(base))

lista_pos = []
for num in range(1,12):
  lista_pos.append(str(num))
lista_pos.append('8.5')
lista_pos.append('9.5')

posicao = st.text_input('Inserir o número da posição desejada (1 a 11):')
if posicao not in lista_pos:
  st.write('Favor inserir posição válida')

min_min = st.text_input('Minutagem mínima para analisar:')

idade_max = st.text_input('Idade máxima para analisar:')

posicao = float(posicao)
min_min = int(min_min)
idade_max = int(idade_max)

dic_posicoes = {1:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                2:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                3:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                4:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                5:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                6:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                7:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                8:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                8.5:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                9:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                9.5:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                10:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90'],
                11:['Golos','Golos esperados','Assistências','Assistências esperadas','Duelos/90']}

dic_siglas = {1:['GK'],
              2:['RB'],
              3:['CB','RCB'],
              4:['CB','LCB'],
              5:['RDMF','LDMF','DMF','LCMF','RCMF','CMF'],
              6:['LB'],
              7:['LW','LAMF','LWF'],
              8:['RDMF','LDMF','DMF','LCMF','RCMF','CMF'],
              8.5:['RDMF','LDMF','DMF','LCMF','RCMF','CMF','AMF','RAMF','LAMF'],
              9:['CF'],
              9.5:['CF','AMF','RAMF','LAMF'],
              10:['AMF','RAMF','LAMF'],
              11:['RW','RAMF','RWF']}


lista_cols = ['Jogador','Equipa','Posição','Idade','Partidas jogadas','Minutos jogados:']

for item in dic_posicoes[posicao]:
    lista_cols.append(item)
    

df_resumo = base[lista_cols].copy()

df_resumo = df_resumo[(df_resumo['Minutos jogados:'] >= min_min)&(df_resumo.Idade<=idade_max)].reset_index(drop=True)

comp = len(df_resumo)

t=0
while t < comp:
    cont = 0
    for item in dic_siglas[posicao]:
        if item in df_resumo['Posição'][t]:
            cont = 1
            continue
        else:
            continue
    if cont == 0:
        df_resumo = df_resumo.drop(t)
    t += 1
    
df_resumo = df_resumo.reset_index(drop=True)
        

df_resumo['ID'] = range(1,len(df_resumo)+1)


st.write(df_resumo)





df_radar = df_resumo[['Jogador','Equipa','Posição','Idade','Partidas jogadas','Minutos jogados:','ID']].copy()

df_radar = df_radar.reset_index(drop=True)

for coluna in dic_posicoes[posicao]:
    df_radar[coluna] = ''
    
    t = 0

    while t < len(df_resumo):
        df_resumo[coluna] = df_resumo[coluna].astype('float64')
        df_radar[coluna][t] = (df_resumo[coluna][t] - np.nanmin(df_resumo[coluna]))/abs(np.nanmax(df_resumo[coluna])-np.nanmin(df_resumo[coluna]))
        t += 1

df_radar = df_radar.replace(np.nan,0).reset_index(drop=True)





df_area = pd.DataFrame()
lista_area = []
lista_jogador = []
lista_clube = []
lista_ids = []

v = 0

while v < len(df_radar):
    
    jogador = df_radar.Jogador[v]
    clube = df_radar.Equipa[v]
    idjog = df_radar.ID[v]
    
    lista_jogador.append(jogador)
    
    aux_df = df_radar[(df_radar.Jogador == jogador)&(df_radar.Equipa == clube)].loc[:, df_radar.columns != 'Jogador']
    aux_df = aux_df.drop('ID',axis=1)
    aux_df = aux_df.loc[:,aux_df.columns != 'Minutos jogados:']
    aux_df = aux_df.loc[:,aux_df.columns != 'Partidas jogadas']
    aux_df = aux_df.loc[:,aux_df.columns != 'Idade']
    aux_df = aux_df.loc[:,aux_df.columns != 'Equipa']
    aux_df = aux_df.loc[:,aux_df.columns != 'Posição']
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

    df_categorias = pd.DataFrame({'raio':lista_raio,'Cat':categories,
                              'theta_n':pd.factorize(categories)[0],
                              'theta_radian':label_loc,
                              'x': lista_raio * np.cos(label_loc),
                              'y': lista_raio * np.sin(label_loc)})
    
    coords  = []
    
    coords.append([lista_raio[0],0])

    t = 1
    
    while t<len(df_categorias):
        coords.append([df_categorias.x[t],df_categorias.y[t]])
        t += 1
        
    coords = coords[:-1]
    
    polygon = Polygon(coords)
    
    area = polygon.area
    
    lista_area.append(area)
    lista_clube.append(clube)
    lista_ids.append(idjog)
    
    v += 1
    
df_area['Jogador'] = lista_jogador
df_area['Area'] = lista_area
df_area['Clube'] = lista_clube
df_area['ID'] = lista_ids

dic_nomes_pos = {1:'Goleiro',
                2:'Lateral Direito',
                3:'Zagueiro',
                4:'Zagueiro',
                5:'Médio Defensivo',
                6:'Lateral Esquerdo',
                7:'Extremo Esquerdo',
                8:'Box to Box',
                8.5:'Médio Ofensivo',
                9:'Centroavante',
                9.5:'Segundo Atacante',
                10:'Meia',
                11:'Extremo Direito'}




df_top = df_area.nlargest(10,'Area')

fig = plt.figure(figsize = (15,9), tight_layout=True)

gs = fig.add_gridspec(10,10)
ax1 = fig.add_subplot(gs[0:1, 0:2])
ax2 = fig.add_subplot(gs[0:1, 1:])

ax3 = fig.add_subplot(gs[1:5, 0:2],polar = True)
ax4 = fig.add_subplot(gs[1:5, 2:4],polar = True)
ax5 = fig.add_subplot(gs[1:5, 4:6],polar = True)
ax6 = fig.add_subplot(gs[1:5, 6:8],polar = True)
ax7 = fig.add_subplot(gs[1:5, 8:10],polar = True)

ax8 = fig.add_subplot(gs[5:10, 0:2],polar = True)
ax9 = fig.add_subplot(gs[5:10, 2:4],polar = True)
ax10 = fig.add_subplot(gs[5:10, 4:6],polar = True)
ax11 = fig.add_subplot(gs[5:10, 6:8],polar = True)
ax12 = fig.add_subplot(gs[5:10, 8:10],polar = True)


lista_axs = [ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12]

ax2.annotate(xy = (0, .5),
    text = "Top "+str(len(df_top))+": Posição "+dic_nomes_pos[posicao]+"\nAnálise Mercado",
    ha = "left",
    va = "center",
    weight = "bold",
    size = 30,color='darkblue')
ax2.axis("off")

v = 0

for jogador in df_top.ID:
    
    aux_df = df_radar[df_radar.ID == jogador].loc[:, df_radar.columns != 'ID']
    aux_df = aux_df.drop('Jogador',axis=1)
    
    nome = df_top[df_top.ID == jogador]['Jogador'].tolist()[0]
    
    minutos = aux_df['Minutos jogados:'].tolist()[0]
    jogos = aux_df['Partidas jogadas'].tolist()[0]
    clube = aux_df['Equipa'].tolist()[0]
    idade = aux_df['Idade'].tolist()[0]
    
    aux_df = aux_df.loc[:,aux_df.columns != 'Minutos jogados:']
    aux_df = aux_df.loc[:,aux_df.columns != 'Partidas jogadas']
    aux_df = aux_df.loc[:,aux_df.columns != 'Idade']
    aux_df = aux_df.loc[:,aux_df.columns != 'Equipa']
    aux_df = aux_df.loc[:,aux_df.columns != 'Posição']
    
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
    
    lista_axs[v].set_title(nome + ' (' + str(minutos) + "')",fontsize = 16,fontweight='bold',color='darkblue')

    lista_axs[v].set_thetagrids(np.degrees(label_loc), labels=categories,fontsize=7.5)
    
    lista_axs[v].set_ylim(0,1)
    
    lista_axs[v].fill(label_loc,lista_raio,alpha=0.3)
    
    v += 1

st.pyplot(fig)
