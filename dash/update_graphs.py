import plotly.graph_objects as go
import pandas as pd
import dash
from numpy import random
from dash import (
    dcc,
    html)
from dash.dependencies import (
    Output,
    Input)

df = pd.read_csv('data/mpg.csv')

df['year'] = random.randint(-4,5,len(df))*0.1 + df['model_year']

app = dash.Dash()


app.layout = html.Div([
    html.Div([
            dcc.Graph(id='mpg-scatter',
    figure={'data':[go.Scatter(
            x=df['year']+1900,
            y=df['mpg'],
            text=df['name'],
            hoverinfo = ['text','y','x'],
            mode = 'markers')],
            'layout':go.Layout(title='MPG Data',
            xaxis={'title':'Model Year'},
            yaxis={'title':'MPG'},
            hovermode='closest')
})
    ], style={'width':'50%','display':'inline-block'}),
    html.Div([
        dcc.Graph(id='mpg_line',
            figure={'data':[go.Scatter(
                    x=[0,1],
                    y=[0,1],
                    mode='lines'
            )],
                    'layout':go.Layout(title='Acceleration',margin={'l':0})})
    ],style={'width':'20%', 'height':'50%','display':'inline-block'}),
    html.Div([
        dcc.Markdown(id='mpg_stats')
    ],style={'width':'20%','height':'50%','display':'inline-block'})
])

@app.callback(Output('mpg_line','figure'),
   [Input('mpg-scatter','hoverData')] )
def calback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data':[go.Scatter(
                    x=[0,1],
                    y=[0,60/df.iloc[v_index]['acceleration']],
                    mode='lines',
                    line = {'width': df.iloc[v_index]['cylinders']}
            )],
        'layout':go.Layout(title=df.iloc[v_index]['name'],
            xaxis = {'visible':False},
            yaxis = {'visible':False,'range':[0,60/df['acceleration'].min()]},
            margin={'l':0},
            height=300)}

    return figure


@app.callback(Output('mpg_stats','children'),
              [Input('mpg-scatter','hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = f"""
        {df.iloc[v_index]['cylinders']} cylinders
        {df.iloc[v_index]['displacement']}cc displacement
        0 to 60mph in {df.iloc[v_index]['acceleration']} seconds
    """

    return stats

if __name__ == '__main__':
    app.run_server()
