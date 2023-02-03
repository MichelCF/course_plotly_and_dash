import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/flights.csv')

data = [go.Heatmap(x=df['year'],y=df['month'],
        z=df['passengers'].values.tolist(),
        colorscale='Jet')]

layout = go.Layout(title ='Fligths')

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='HTML/Heatmap_Exercise.html')