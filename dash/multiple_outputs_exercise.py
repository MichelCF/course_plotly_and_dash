import dash
from dash import dcc, html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider( id='range-slider', value=[0,0], min=-5, max=5, step=1),
    html.Div(id='range-slider-output',style={'fontSize': 30,"font-weight": "bold"})
])

@app.callback(
    Output('range-slider-output', 'children'),
    [Input('range-slider', 'value')])
def update_output(value):
    left_value = value[0]
    right_value = value[1]
    return left_value*right_value

if __name__ == '__main__':
    app.run_server()