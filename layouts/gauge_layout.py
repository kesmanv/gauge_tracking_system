# Naming convention
# Component ID = 'component-name-example'


import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
from dash.exceptions import PreventUpdate
from dash_extensions import Download
import pandas as pd
from dash.dependencies import Input, Output, State
from app import app
from layouts import plots, cards, navigation_bar, filters
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
blue_btn_style = {
    'background-color': '#007ace'  
    ,'color': 'white'
    ,'border-radius':'4px'
    ,'border': '1px solid white'
    ,'height': '38px'
    ,'padding': '0 30px'
    #,'font-size': '11px'
}
#####################################################################################################################
####################################### Gauge App - Table of records ################################################
#####################################################################################################################


# Table records
gauge_table = dash_table.DataTable(
                                            
                                id='gauge-table' 
                                ,data = tf.df.to_dict('rows')
                                ,columns=[
                                        {'name':'Plant'
                                        ,'id':'Plant'}
                                        ,{'name': 'Gauge ID'
                                        ,'id': 'Gage ID'
                                        }, {
                                                'name':'Description'
                                                ,'id': 'Description'
                                        }, {
                                                'name':'Gauge S/N'
                                                ,'id': 'Gage S/N'
                                        }, {
                                                'name':'Asset No'
                                                ,'id': 'Asset No'
                                        }, {
                                                'name':'Model No.'
                                                ,'id': 'Model No.'
                                        },{
                                                'name':'Current Location'
                                                ,'id': 'Current Location'
                                        }, {
                                                'name':'Manufacturer'
                                                ,'id': 'Manufacturer'
                                        }, {
                                                'name':'Last Calibration By'
                                                ,'id': 'Last Calibrated By'
                                        } , {
                                                'name':'Last Calibration Date'
                                                ,'id': 'Last Cal Date'
                                        }, {
                                                'name':'Next Due Date'
                                                ,'id': 'Next Due Date'
                                                ,'type': 'datetime'
                                        }
                                        ]
                                        ,page_size=20
                                        ,style_cell_conditional=[
                                                                {'if': {'column_id':'Plant'}, 'width':'60px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Gage ID'}, 'width':'100px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Description'}, 'width':'280px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Gage S/N'}, 'width':'120px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Asset No'}, 'width':'80px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Model No.'}, 'width':'80px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Current Location'}, 'width':'140px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Manufacturer'}, 'width':'100px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Last Calibrated By'}, 'width':'180px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Last Cal Date'}, 'width':'170px', 'textAlign':'center'}
                                                                ,{'if': {'column_id':'Next Due Date'}, 'width':'130px', 'textAlign':'center'}
                                        ]
                                        ,style_header={'fontWeight':'bold'}
                                        ,sort_action='native' 
                                        ,cell_selectable=True
                                        #,editable=True
                                        #,filter_action='native'
                                        # ,style_data_conditional=[{
                                        #         'if':{
                                        #                 'filter_query':'{Due Soon} contains "Yes"'
                                        #         }, 'column_id':'Plant', 'backgroundColor':'#ffeeb2'
                                        # }]

                                                
                                         
)

# gauge_table_updated = dash_table.DataTable(
#         id = 'gauge-table-updated'
# )

#####################################################################################################################
####################################### Gauge App - Main Layout #####################################################
#####################################################################################################################

layout = html.Div([
    
    #######################################
    ########## Navigation Bar #############
    #######################################
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
            #######################################
            ########## Current App Header #########
            #######################################
            ,dbc.Col(
                dbc.Row(
                    dbc.Col([
                        html.Div(
                            [html.H1('Food NA - Gauge Tracking System')]
                            ,style={'text-align':'center','margin-bottom':80}
                        )
                        #############################
                        ####### Gauges TABS ################
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
                                ,html.Br()
                                ,html.Div(
                                    id='gauge-save-button-div'
                                    ,children = html.Button(
                                        'Save'
                                        ,id='gauge-save-button'
                                        #, style={'display', 'none'}
                                        ) 
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

#####################################################################################################################
####################################### Callbacks ###################################################################
#####################################################################################################################



# Tabs callback
@app.callback(
    [
        Output('tabs-gauge-content', 'children')
        ,Output('tb-download-btn', 'children')
    ]
    ,[
        Input('tabs-gauge', 'active_tab') # dcc.Tabs
    ]
)
def tab_gauge_content(active_tab):
    if active_tab=='tab-gauge-records':
        download_btn = html.Div([html.Button("Download records", id="download-btn", style=white_btn_style), Download(id="download")]) 
        return gauge_table, download_btn
    elif active_tab=='tab-add-gauge':
        return html.H2('New Gauge placeholder'), html.Br()
    elif active_tab=='tab-gauge-studies':
        return html.H2('Gauge studies placeholder'), html.Br()
    elif active_tab=='tab-gauge-capabilities':
        return html.H2('Gauge capabilities placeholder'), html.Br()

#Make table editable
@app.callback(
    [Output('gauge-table', 'editable')
    ,Output('gauge-save-button', 'style')]
    ,[Input('make-gauge-table-editable', 'value')] 
    
)
def make_gauge_tbl_editable(value):
    if value == []:
        style = {'display':'none'}
        return False, style
    elif value == ['Y']:
        style = blue_btn_style
        return True, style

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
        Input('download-btn', 'n_clicks')
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
    

#Update gauge records table with user edits
@app.callback(
    [
        Output('table-updated', 'children')
    ]
    ,[
        
        Input('gauge-table', 'active_cell')
        ,Input('gauge-table', 'data')
        ,Input('gauge-table', 'data_previous')
        ,Input('make-gauge-table-editable', 'value')
        ,Input('gauge-save-button', 'n_clicks')
        
    ]
)
def update_gauge_table(active_cell, data, data_previous, editable, clicks):
        
    if editable == ['Y']:
        if active_cell is not None:
            tf.changed_cells['row_id'].append(active_cell['row_id'])
            tf.changed_cells['column_id'].append(active_cell['column_id'])
            
        return ['tracking']   
    else:
        return ['nothing tracked']


    
    # if clicks is None:
    #     updated_table = ['Not updated yet']
    #     return updated_table
    # else:

    
