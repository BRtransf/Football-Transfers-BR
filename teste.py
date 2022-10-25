import streamlit as st
import pandas as pd

base = pd.concat([pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

st.write(len(base))



posicao = float(st.text_input('Inserir o número da posição desejada (1 a 11):'))

min_min = int(st.text_input('Minutagem mínima para analisar:'))

idade_max = int(st.text_input('Idade máxima para analisar:'))
