import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter(x=df['acceleration'],
    y=df['model_year']/100,text=df['name'],
    mode='markers',
    marker=dict(size=df['displacement']/10,
     color=df['mpg'],
     showscale=True))]

layout = go.Layout(title='Acceleration x Model Year', hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='HTML/BubbleChartExercise.html')