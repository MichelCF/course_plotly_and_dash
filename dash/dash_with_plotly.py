import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
np.random.seed(14)
random_x =np.random.randint(1,101,100)
random_y =np.random.randint(1,101,100)

graph1 = dcc.Graph(id='scatterplot',
            figure = {
                'data':[
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode='markers',
                        marker = {
                            'size':12,
                            'color':'rgb(51,204,153)',
                            'symbol':'pentagon',
                            'line':{'width':2}
                        }
                    )],
                'layout':go.Layout(title='My Scartterplot',
                                    xaxis = {'title':'Some X title'})
            })

graph2 = dcc.Graph(id='lineplot',
            figure = {
                'data':[
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode='lines',
                    )],
                'layout':go.Layout(title='Line Plot',
                                    xaxis = {'title':'Some X title'})
            })

app = dash.Dash()


app.layout = html.Div([
    graph1,
    graph2])

if __name__ =='__main__':
    app.run_server()