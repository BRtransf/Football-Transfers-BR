import streamlit as st
import pandas as pd
import numpy as np

base = pd.concat([pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

      
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
        df_resumo[coluna] = df_resumo[coluna].astype('int')
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

