import dash
from dash import dcc, html
from dash.dependencies import Input,Output
import plotly.graph_objects as go
import pandas as pd
import json
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return f'data:image/png;base64,{encoded.decode()}'

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

scatter = go.Scatter(x=df['color'],
    y=df['wheels'],
    dy = 1,
    mode='markers',
    marker={'size':15})

app.layout = html.Div([
    html.Div(dcc.Graph(id='wheels-plot',
        figure={
            'data':[scatter],
            'layout':go.Layout(title='Test', hovermode='closest')
        },style={'width':'30%','float':'left'})),
    html.Div(html.Img(id='hover-data',
    src='children',
    style={'width':'30%'}),
    style={'paddingTop':35})
])


@app.callback(Output('hover-data','src'),
    [Input('wheels-plot','hoverData')])
def callacl_image(hoverData):
    path = '../data/Images/'
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()