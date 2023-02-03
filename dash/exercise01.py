import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('../data/OldFaithful.csv')
graph1 = dcc.Graph(id='oldfaithful',
            figure = {
                'data':[
                    go.Scatter(
                        x=df['X'],
                        y=df['Y'],
                        mode='markers',
                        marker = {
                            'size':12,
                            'color':'rgb(138,43,226)',
                            'line':{'width':1}
                        }
                    )],
                'layout':go.Layout(title='Old Faithful Eruptions Intervals X Durations',
                                    xaxis = {'title':'Duration of eruption (minutes'},
                                    yaxis = {'title':'Interval to next eruption (minutes'})
            })

app = dash.Dash()


app.layout = html.Div([
    graph1
    ])

if __name__ =='__main__':
    app.run_server()