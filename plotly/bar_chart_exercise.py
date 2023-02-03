import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mocksurvey.csv', index_col=0)

#Vertical
#data = [go.Bar(x=df.index, y=df[response],name=response) for response in df.columns]

#Horizontal
data = [go.Bar(x=df[response], y=df.index,name=response,orientation='h') for response in df.columns]

layout = go.Layout(title='Questions', barmode='stack')

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='HTML/BarChartExercise.html')
