# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # -------PreBuiltModel-------
    html.H3(
        children='PreBuilt-Model',
        style={
            'textAlign': 'left'
        }
    ),

    html.Label('Dataset'),
    dcc.Dropdown(
        options=[
            {'label': 'Ames Housing', 'value': 'ames'},
            {'label': 'Crittendent County AR', 'value': 'AR'}
        ],
        value='ames'
    ),

    html.Label('Model'),
    dcc.Dropdown(
        options=[
            {'label': 'Populate according to dataset.', 'value':'default'},
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='default'
    ),

    html.Label('Address'),
    dcc.Dropdown(
        id = 'pb-model-address',
        options=[
            {'label': 'TestAddress0', 'value':'123 Front St., Memphis, TN'},
            {'label': 'TestAddress1', 'value':'456 Hello World St, West Memphis, AR'}
        ],
        value='Please select an address'
    ),

    html.Label('Predicted Price'),
    dcc.Input(id='pb-model-predicted', value='', type='text'),
    html.Label('Actual Price'),
    dcc.Input(id='pb-model-actual', value='', type='text'),
    # -------End-of-PreBuiltModel-------

    # -------Live-model-------
    html.H3(
        children='Live Model',
        style={
            'textAlign': 'left'
        }
    ),

    html.Label('Dataset'),
    dcc.Dropdown(
        options=[
            {'label': 'Crittendent County AR', 'value': 'AR'},
            {'label': 'Ames Housing', 'value': 'ames'}
        ],
        value='ames'
    ),

    html.Label('Features'),
    dcc.Checklist(
        options=[
            {'label': 'Zip', 'value': 'NYC'},
            {'label': 'School District', 'value': 'MTL'},
            {'label': 'These check boxes will be populated according to Dataset', 'value': 'SF'}
        ],
        values=['MTL', 'SF']
    ),

    html.Label('Predicted Price'),
    dcc.Input(id='live-model-predicted', value='', type='text'),

    html.Label('Actual Price of similar/same property pulled from Zillow:'),
    dcc.Input(id='live-model-actual', value='', type='text'),
    # -------End-of-Live-model-------

    # -------Shopping-helper--------
    html.H3(
        children='Shopping Helper',
        style={
            'textAlign': 'left'
        }
    ),

    html.Label('Your budget'),
    dcc.Input(id='sh-input-budget', value='', type='text'),
    
], style={'columnCount': 1})

@app.callback(
    Output(component_id='pb-model-predicted', component_property='value'),
    [Input(component_id='pb-model-address', component_property='value')]
)
def predict_price_on_address_select(input_value):
    return input_value

@app.callback(
    Output(component_id='pb-model-actual', component_property='value'),
    [Input(component_id='pb-model-address', component_property='value')]
)
def actual_price_on_address_select(input_value):
    return input_value


if __name__ == '__main__':
    app.run_server(debug=True)

