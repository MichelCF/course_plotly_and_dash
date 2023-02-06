import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/gapminderDataFiveYear.csv')

year_options = [{'label':str(year),'value':year} for year in df['year'].unique()]

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
        options=year_options,
        value=df['year'].min())
])

@app.callback(Output('graph','figure'),
    [Input('year-picker','value')])
def update_figure(selected_year):

    filtered_df = df[df['year'] == selected_year]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name]
        traces.append(go.Scatter(
            x = df_by_continent['gdpPercap'],
            y = df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker = {'size':15},
            name=continent_name
        ))

    return {'data': traces,
        'layout':go.Layout(
            title = 'gpdPercap X lifeExp',
            xaxis={'title':'GPD Per Cap',
            'type':'log'},
            yaxis={'title':'Life Expectancy'}
        )}

if __name__ == '__main__':
    app.run_server()