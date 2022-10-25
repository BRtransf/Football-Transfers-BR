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

dic_posicoes = {1:['Minutos jogados:'],
                2:['Minutos jogados:'],
                3:['Minutos jogados:'],
                4:['Minutos jogados:'],
                5:['Minutos jogados:'],
                6:['Minutos jogados:'],
                7:['Minutos jogados:'],
                8:['Minutos jogados:'],
                8.5:['Minutos jogados:'],
                9:['Minutos jogados:'],
                9.5:['Minutos jogados:'],
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

st.write(df_resumo)


df_resumo = df_resumo[(df_resumo['Minutos jogados:'] >= min_min)&(df_resumo.Idade<=idade_max)].reset_index(drop=True)











