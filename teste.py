import streamlit as st
import pandas as pd

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

dic_posicoes = {1:['Golos'],
                2:['Golos'],
                3:['Golos'],
                4:['Golos'],
                5:['Golos'],
                6:['Golos'],
                7:['Golos'],
                8:['Golos'],
                8.5:['Golos'],
                9:['Golos'],
                9.5:['Golos'],
                10:['Minutos jogados:'],
                11:['Minutos jogados:']}

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







