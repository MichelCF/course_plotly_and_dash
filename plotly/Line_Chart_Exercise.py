import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/Yuma.csv')
days =['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
x_axies= df[df['DAY'] == 'SUNDAY']['LST_TIME']

data = [go.Scatter(x=df['LST_TIME'],
    y=df[df['DAY'] == day]['T_HR_AVG'],
    mode='lines',
    name=day) for day in days]

pyo.plot(data, filename='HTML/LineChartsExercise.html')