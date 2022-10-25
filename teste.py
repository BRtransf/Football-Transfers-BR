import streamlit as st
import pandas as pd

base = pd.concat([pd.read_csv('base1.csv',sep=';'),pd.read_csv('base2.csv',sep=';')]).drop_duplicates(['Jogador','Equipa','Minutos jogados:'])

st.write(len(base))

base['DefesaMeta'] = (base['Golos sofridos esperados/90']/base['Golos sofridos/90'])*(base['Remates sofridos/90']*base['Defesas, %'])
base['EstiloPasse'] = base['Passes longos/90']/base['Passes curtos / médios /90']

## zagueiros
base['Abordagem Agressiva'] = base['Faltas/90'] / (base['Duelos defensivos/90']*base['Duelos defensivos ganhos, %'])
base['Duelos Aéreos Ganhos'] = base['Duelos aérios/90']*base['Duelos aéreos ganhos, %']
base['Construção'] = (base['Passes para a frente certos, %']*base['Passes para a frente/90'])/(base['Passes/90']*base['Passes certos, %'])

## laterais
base['Dribles Certos'] = base['Dribles/90']*base['Dribles com sucesso, %']
base['Cruzamentos Certos'] = base['Cruzamentos/90']*base['Cruzamentos certos, %']
base['Tendência Cruzamento'] = base['Cruzamentos/90']/base['Passes recebidos/90']
base['Duelos Defensivos Ganhos'] = base['Duelos defensivos/90']*base['Duelos defensivos ganhos, %']

## medio defensivo
base['DistSobPressão'] = (base['Passes/90']*base['Passes certos, %']) / (base['Passes recebidos/90']/base['Duelos ofensivos/90'])

## box to box
base['Desarme Intercep'] = base['Duelos defensivos/90'] + base['Interseções/90']
base['Duelos Ofensivos Ganhos'] = base['Duelos ofensivos/90']*base['Duelos ofensivos ganhos, %']
base['Participação'] = base['Duelos Defensivos Ganhos'] + base['Duelos Ofensivos Ganhos']
base['Infiltração Finalização'] = base['Toques na área/90'] / base['Remates/90']

## medio ofensivo
base['Infiltração xG'] = base['Toques na área/90'] * base['Golos esperados/90']
base['Dribles Certos'] = base['Dribles/90']*base['Dribles com sucesso, %']

## meia
base['Associação'] = (base['Passes/90']*base['Passes certos, %'])/base['Passes recebidos/90']

## extremos
base['GolxG'] = base['Golos'] / base['Golos esperados']
base['Finalização'] = base['Remates/90']*base['Remates à baliza, %']
base['Cruzamento Efetivo'] = base['Assistências esperadas/90']/base['Cruzamentos Certos']

## SA
base['Assistência'] = base['Assistências esperadas/90']/base['Assistências para remate/90']

## CA
base['Pivo'] = (base['Passes/90']*base['Passes certos, %'] + base['Dribles Certos'])



posicao = float(st.text_input('Inserir o número da posição desejada (1 a 11):'))

min_min = int(st.text_input('Minutagem mínima para analisar:'))

idade_max = int(st.text_input('Idade máxima para analisar:'))
