import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2019-alldata.csv')
df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME',inplace=True)
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]
print(df2.columns)
print(df2.index)

