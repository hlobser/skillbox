
import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Нажми меня!', id='my-button'),
    html.Div(id='my-output')
])

@app.callback(Output('my-output', 'children'),
              Input('my-button', 'n_clicks'))
def update_output(n_clicks):
    if n_clicks is None:
        return ''
    else:
        return f'Кнопка была нажата {n_clicks} раз!'

if __name__ == '__main__':
    app.run_server(debug=True)