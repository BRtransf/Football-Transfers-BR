import streamlit as st
import pandas as pd

base = pd.concat([pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

st.write(len(base))



posicao = st.text_input('Inserir o número da posição desejada (1 a 11):')

min_min = st.text_input('Minutagem mínima para analisar:')

idade_max = st.text_input('Idade máxima para analisar:')


posicao = float(posicao)
min_min = int(min_min)
idade_max = int(idade_max)
