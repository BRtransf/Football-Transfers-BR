import streamlit as st
import pandas as pd

base = pd.concat([pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

def trat_base_wyscout(base):
  for coluna in base.columns:
    if type(base[coluna][0]) == 'int':
      base[coluna] = base[coluna].astype('int')
      
trat_base_wyscout(base)

base['DefesaMeta'] = (base['Golos sofridos esperados/90']/base['Golos sofridos/90'])*(base['Remates sofridos/90']*base['Defesas, %'])
      
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

