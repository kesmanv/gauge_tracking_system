# Naming convention
# Component ID = 'component-name-example'


import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.exceptions import PreventUpdate
from dash_extensions import Download
import pandas as pd
from dash.dependencies import Input, Output
from app import app
from layouts import plots, cards, tables, navigation_bar, filters
from database import transforms as tf
import plotly.graph_objects as go

import io # Used for downloading csv file

white_btn_style = {
    'background-color': '#e6e6e6'
    ,'color': 'black'
    ,'border-radius':'4px'
    ,'border': '1px solid #bbb'
    ,'height': '38px'
    ,'padding': '0 30px'
    #,'font-size': '11px'
}

layout = html.Div([
    html.Div(navigation_bar.nav)
    ,dbc.Row(
            [
            dbc.Col(
                [
                    filters.common_filters
                    ,filters.gauge_filters
                ]
                , width=2
                , style={
                    'margin-top':165
                    ,'margin-bottom':2200
                    #,'backgroundColor':'gray'
                }
            )    
            ,dbc.Col(
                dbc.Row(
                    dbc.Col([
                        html.Div(
                            [html.H1('Food NA - Gauge Tracking System')]
                            ,style={'text-align':'center','margin-bottom':80}
                        )
                        ,dbc.Row(html.Div(
                            [
                                dbc.Tabs(
                                    id='tabs-gauge'
                                    ,active_tab='tab-gauge-records'
                                    ,children=[
                                        dbc.Tab(label='Gauge Records', tab_id='tab-gauge-records')
                                        ,dbc.Tab(label='Add Gauge', tab_id='tab-add-gauge')
                                        ,dbc.Tab(label='Gauge Studies', tab_id='tab-gauge-studies')
                                        ,dbc.Tab(label='Gauge Capabilities', tab_id='tab-gauge-capabilities')
                                    ]
                                )
                                ,html.Div(
                                    id='tabs-gauge-content'
                                    ,style={'padding': '5px 5px 0px 5px'} # padding: Top,Right,Bottom,Left
                                )
                                   
                            ] )   
                        ,style={
                            'margin-right':-5
                            ,'margin-left':10  
                        }   
                        )    
                    ]
                    )
                )#, style={'backgroundColor':'gray'}
            )
    ], style={'margin-right':10,'margin-left':10, 'margin-top':0})
]
)



# Tabs callback
@app.callback(
    [
        Output('tabs-gauge-content', 'children')
        ,Output('tb-download-btn', 'children')
    ]
    ,[Input('tabs-gauge', 'active_tab')]
)
def tab_gauge_content(active_tab):
    if active_tab=='tab-gauge-records':
        btn = html.Div([html.Button("Download records", id="btn", style=white_btn_style), Download(id="download")]) 
        return tables.gauge_table, btn
    elif active_tab=='tab-add-gauge':
        return html.H2('New Gauge placeholder')
    elif active_tab=='tab-gauge-studies':
        return html.H2('Gauge studies placeholder')
    elif active_tab=='tab-gauge-capabilities':
        return html.H2('Gauge capabilities placeholder')



# Gauge records filters
@app.callback(Output('gauge-table', 'data')
    ,[
        Input('plant', 'value')
        ,Input('gauge-manufacturer', 'value')
        ,Input('gauge-type', 'value')
        ,Input('gauge-due-soon', 'value')   
    ]
)

def tb_gauge_filters(plant, mfg, g_type, due):
    filters_input = {'Plant': plant, 'Manufacturer':mfg, 'Type':g_type, 'Due Soon': due}
    filtered_dict = {k:v for k,v in filters_input.items() if len(v)!=0}

    if len(filtered_dict)==0:
        return tf.df.to_dict('rows')
    else:
        filtered_table = tf.df.copy()
        for k,v in filtered_dict.items():
            filtered_table = filtered_table.loc[filtered_table[k].isin(v)] 
        return filtered_table.to_dict('rows')                               

# Dynamic dropdown list (gauge filters)
@app.callback(
    [
        Output('gauge-manufacturer', 'options')
        ,Output('gauge-type', 'options') 
    ]
    ,[
        Input('plant', 'value')
        ,Input('gauge-type', 'value')
    ]
)

def set_gauge_mfg_options(plant, gauge_type): 
    if len(plant) == 0:

        mfg_options = tf.drop_options(tf.gauge_manufacturer)
        type_options = tf.drop_options(tf.gauge_types)
        return mfg_options, type_options
    else:
        # Gauge manufacturer dropdown options
        df_ = tf.df.loc[tf.df['Plant'].isin(plant)==True, ['Manufacturer', 'Type']]
        df_mfg = df_['Manufacturer'].dropna().unique()
        mfg_options = tf.drop_options(df_mfg)
        
        # Gauge type dropdown options
        df_type = df_['Type'].dropna().unique()
        type_options = tf.drop_options(df_type)
        
        return  mfg_options, type_options


# Download table (csv)
@app.callback(
    Output('download', 'data'), 
    [
        Input('btn', 'n_clicks')
        ,Input('gauge-table', 'data')
    ]
)
def generate_csv(n_clicks, data):
    if n_clicks is not None and tf.current_clicks != n_clicks:
        s = io.StringIO()
        pd.DataFrame.from_dict(data).to_csv(s, index=False)
        content=s.getvalue()
        tf.current_clicks = n_clicks
        return dict(filename='data.csv', content=content, type='text/csv')
    
