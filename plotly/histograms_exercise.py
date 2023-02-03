import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/abalone.csv')

data = [go.Histogram(x=df['length'],
    xbins=dict(start=0,end=1,size=.02))]
layout = go.Layout(title='Shell lengths from Abalone dataset', title_x=0.5)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='HTML/Histograms_Exercise.html')