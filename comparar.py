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
base = base.reset_index(drop=True)

st.subheader('Resumo da Base de Dados')
st.write(base[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])

st.subheader('Busca Rápida')
pesq_rap = st.text_input('Digite o nome desejado:')

lista_results = []
nomes = pd.unique(base.Jogador).tolist()
t = 0
while t<len(nomes):
  if pesq_rap in nomes[t]:
    lista_results.append(nomes[t])
  t += 1

st.write(base[base.Jogador.isin(lista_results)][['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])

st.subheader('Jogador 1')
nome_busca1 = st.text_input("Nome do primeiro jogador:")

if len(base[base.Jogador==nome_busca1]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(pd.unique(base[base.Jogador==nome_busca1]['Equipe atual']))>1:
  st.write("Mais de um jogador disponível com este nome, favor inserir o clube atual do jogador desejado.")
  st.write(base[base.Jogador==nome_busca1][['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
  clube1 = st.text_input("Clube do primeiro jogador:")
  if len(pd.unique(base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)]['Idade']))>1:
    st.write("Mais de um jogador disponível com este nome/clube, favor inserir a idade atual do jogador desejado.")
    st.write(base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)][['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
    idade1 = int(st.text_input("Idade do primeiro jogador:"))
    st.write("Tabela resumo do jogador desejado:")
    base1 = base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)&(base.Idade==idade1)]
    st.write(base1[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
  else:
    base1 = base[(base.Jogador==nome_busca1)&(base["Equipe atual"] == clube1)]
    st.write("Tabela resumo do jogador desejado:")
    st.write(base1[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
                 
else:
    base1 = base[base.Jogador == nome_busca1]
    st.write("Tabela resumo do jogador desejado:")
    st.write(base1[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])

base1 = base1.assign(ID = 1)    

st.subheader('Jogador 2')    
nome_busca2 = st.text_input("Nome do segundo jogador:")

if len(base[base.Jogador==nome_busca2]) == 0:
  st.write("Favor inserir o nome do jogador igual no WyScout")

elif len(pd.unique(base[base.Jogador==nome_busca2]['Equipe atual']))>1:
  st.write("Mais de um jogador disponível com este nome, favor inserir o clube atual do jogador desejado.")
  st.write(base[base.Jogador==nome_busca2][['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
  clube2 = st.text_input("Clube do segundo jogador:")
  if len(pd.unique(base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)]['Idade']))>1:
    st.write("Mais de um jogador disponível com este nome/clube, favor inserir a idade atual do jogador desejado.")
    st.write(base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)][['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
    idade2 = int(st.text_input("Idade do segundo jogador:"))
    base2 = base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)&(base.Idade==idade2)]
    st.write("Tabela resumo do jogador desejado:")
    st.write(base2[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
  else:
    base2 = base[(base.Jogador==nome_busca2)&(base["Equipe atual"] == clube2)]
    st.write("Tabela resumo do jogador desejado:")
    st.write(base2[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])
                 
else:
    base2 = base[base.Jogador == nome_busca2]
    st.write("Tabela resumo do jogador desejado:")
    st.write(base2[['Jogador','Equipe atual','Equipe no ano','Minutos jogados:','Ano']])    

base2 = base2.assign(ID = 2)       

ano1min = int(np.nanmin(base1.Ano))
ano1max = int(np.nanmax(base1.Ano))
ano2min = int(np.nanmin(base2.Ano))
ano2max = int(np.nanmax(base2.Ano))

if ano1min < ano1max:
  anos1 = st.slider('Anos analisados para '+nome_busca1,ano1min, ano1max, (ano1min, ano1max))
  st.write('Values:', anos1)
else:
  st.write(nome_busca1 + " somente disponível em "+str(ano1min))
  anos1 = [ano1min,ano1max]

if ano2min < ano2max:
  anos2 = st.slider('Anos analisados para '+nome_busca2,ano2min, ano2max, (ano2min, ano2max))
  st.write('Values:', anos2)
else:
  st.write(nome_busca2 + " somente disponível em "+str(ano2min))
  anos2 = [ano2min,ano2max]

df = pd.concat([base1[(base1.Ano>=anos1[0])&(base1.Ano<=anos1[1])],base2[(base2.Ano>=anos2[0])&(base2.Ano<=anos2[1])]])

vars = st.multiselect(label = 'Variáveis de comparação',options=df.columns[7:])
lista_vars = ['ID','Jogador','Equipe atual','Equipe no ano','Posição','Idade']
for var in vars:
  lista_vars.append(str(var))
  
df_comp = df[lista_vars].copy()

st.write(df_comp)

lista_ranges = []

for coluna in df_comp.columns[6:]:
  top1 = df_comp[df_comp.ID == pd.unique(df_comp.ID)[0]][coluna].sum()
  top2 = df_comp[df_comp.ID == pd.unique(df_comp.ID)[1]][coluna].sum()
  
  if top1 > top2:
    lista_ranges.append((0.85*np.nanmin(df_comp[coluna]),top1*1.1))
  elif top2 >= top1:
    lista_ranges.append((0.85*np.nanmin(df_comp[coluna]),top2*1.1))
    

def _invert(x, limits):
    """inverts a value x on a scale from
    limits[0] to limits[1]"""
    return limits[1] - (x - limits[0])

def _scale_data(data, ranges):
    """scales data[1:] to ranges[0],
    inverts if the scale is reversed"""
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        assert (y1 <= d <= y2) or (y2 <= d <= y1)
    x1, x2 = ranges[0]
    d = data[0]
    if x1 > x2:
        d = _invert(d, (x1, x2))
        x1, x2 = x2, x1
    sdata = [d]
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        if y1 > y2:
            d = _invert(d, (y1, y2))
            y1, y2 = y2, y1
        sdata.append((d-y1) / (y2-y1) 
                     * (x2 - x1) + x1)
    return sdata

class ComplexRadar():
    def __init__(self, fig, variables, ranges,
                 n_ordinate_levels=6):
        angles = np.arange(0, 360, 360./len(variables))

        axes = [fig.add_axes([0.1,0.1,0.9,0.9],polar=True,
                label = "axes{}".format(i)) 
                for i in range(len(variables))]
        l, text = axes[0].set_thetagrids(angles, 
                                         labels=variables)
        [txt.set_rotation(angle-90) for txt, angle 
             in zip(text, angles)]
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i], 
                               num=n_ordinate_levels)
            gridlabel = ["{}".format(round(x,2)) 
                         for x in grid]
            if ranges[i][0] > ranges[i][1]:
                grid = grid[::-1] # hack to invert grid
                          # gridlabels aren't reversed
            gridlabel[0] = "" # clean up origin
            ax.set_rgrids(grid, labels=gridlabel,
                         angle=angles[i])
            #ax.spines["polar"].set_visible(False)
            ax.set_ylim(*ranges[i])
        # variables for plotting
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]
    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)
    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)
        
        
        
categorias = lista_vars[6:]

fig = plt.figure(figsize = (8,8))

radar = ComplexRadar(fig,categorias,lista_ranges)

for jogador in pd.unique(df_comp.ID):
    nome = df_comp[df_comp.ID == jogador]['Jogador'].tolist()[0]
    
    aux_df = df_comp[df_comp.ID == jogador].loc[:, df_comp.columns != 'Jogador']
    aux_df = aux_df.loc[:, aux_df.columns != 'Equipe atual']
    aux_df = aux_df.loc[:, aux_df.columns != 'Equipe no ano']
    aux_df = aux_df.loc[:, aux_df.columns != 'Posição']
    aux_df = aux_df.loc[:, aux_df.columns != 'Idade']
    aux_df = aux_df.loc[:, aux_df.columns != 'ID']
    
    aux_df = aux_df.reset_index(drop=True)
    
    lista_valores = []
    
    for coluna in aux_df.columns:
      lista_valores.append(aux_df[coluna].sum())
    
    radar.plot(lista_valores,label=nome)
    

fig.legend()
    
st.pyplot(fig)

''' está aparecendo só a primeira linha de cada jogador, precisa somar'''
