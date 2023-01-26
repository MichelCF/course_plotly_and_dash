import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('data/abalone.csv')

sample_01 = np.random.choice(df['rings'],10,replace=False)
sample_02 = np.random.choice(df['rings'],10,replace=False)

data = [go.Box(y=sample_01, name='Sample 1',boxpoints='all',pointpos=0),
        go.Box(y=sample_02, name='Sample 2',boxpoints='all',pointpos=0)]

layout = go.Layout(title='Comparing two samples of rings')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='HTML/BoxPlotExercise.html')