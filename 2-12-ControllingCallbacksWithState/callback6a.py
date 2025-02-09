#######
# A very basic Input/Output callback, with State!
######
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize':28}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize':28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('number-in', 'value')])
def output(n_clicks, number):
    return number*2

if __name__ == '__main__':
    app.run_server(debug=True)
