# Naming convention
# Component ID = 'component-name-example'


import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.exceptions import PreventUpdate
#import dash_table
import pandas
from dash.dependencies import Input, Output
from app import app
from layouts import plots, cards, tables, navigation_bar, filters
from database import transforms as tf
import plotly.graph_objects as go


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
    Output('tabs-gauge-content', 'children')
    ,[Input('tabs-gauge', 'active_tab')]
)
def tab_gauge_content(active_tab):
    if active_tab=='tab-gauge-records':
        return tables.gauge_table 
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
    ]
)
def tb_manufacturer_filter(plant, mfg, g_type):
    if (len(plant) == 0) and (len(mfg)==0) and (len(g_type)==0): 
        return tf.df.to_dict('rows')
    elif (len(plant) != 0) and (len(mfg)==0) and (len(g_type)==0):
        filtered_table = tf.df.loc[(tf.df['Plant'].isin(plant)==True)]
        return filtered_table.to_dict('rows')
    elif (len(plant) != 0) and (len(mfg)!=0) and (len(g_type)==0):
        filtered_table = tf.df.loc[(tf.df['Plant'].isin(plant)==True) 
                                    & (tf.df['Manufacturer'].isin(mfg)==True)]
        return filtered_table.to_dict('rows')
    elif (len(plant) != 0) and (len(mfg)!=0) and (len(g_type)!=0):
        filtered_table = tf.df.loc[(tf.df['Plant'].isin(plant)==True) 
                                    & (tf.df['Manufacturer'].isin(mfg)==True) 
                                    & (tf.df['Type'].isin(g_type)==True)]
        return filtered_table.to_dict('rows')
    elif (len(plant) == 0) and (len(mfg)!=0) and (len(g_type)!=0):
        filtered_table = tf.df.loc[(tf.df['Manufacturer'].isin(mfg)==True)
                                    & (tf.df['Type'].isin(g_type)==True)]
        return filtered_table.to_dict('rows')
    elif (len(plant) == 0) and (len(mfg)==0) and (len(g_type)!=0):
        filtered_table = tf.df.loc[tf.df['Type'].isin(g_type)==True]
        return filtered_table.to_dict('rows')
    elif (len(plant) != 0) and (len(mfg)==0) and (len(g_type)!=0):
        filtered_table = tf.df.loc[(tf.df['Plant'].isin(plant)==True)
                                    & (tf.df['Type'].isin(g_type)==True)]
        return filtered_table.to_dict('rows')
    else:
        filtered_table = tf.df.loc[tf.df['Manufacturer'].isin(mfg)==True]
        return filtered_table.to_dict('rows')

# Due Soon Only filter
# @app.callback(
#     Output('gauge-table', 'data')
#     ,[Input('gauge-due-soon', 'options')]
# )
# def gauges_due_soon(dso):
#     if len(dso)==0:
#         return tf.df.to_dict('rows')
#     else:
#         due_soon = tf.due_date_next(tf.df)
#         return due_soon.to_dict()                                    

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