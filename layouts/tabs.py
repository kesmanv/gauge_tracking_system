import dash_table
import pandas as pd
from database import transforms as tf
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from database import transforms as ts

cols = ['Gage ID', 'Description', 'Gage S/N', 'Asset No', 'Current Location', 'Manufacturer'
        ,'Last Calibrated By', 'Last Cal Date', 'Next Due Date']


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

#############################################################################################################################################
############################################### Add New Gauge ###############################################################################
#############################################################################################################################################

input_style_label = {
        'margin-top': '20px'
        ,'margin-botton': '20px'
        ,'margin-left': '60px'
        }
input_style_field = {
        'margin-top': '14px'
        ,'margin-botton': '14px'
        }

input_style_label_date = {
        'margin-top': '37px'
        ,'margin-botton': '37px'
        ,'margin-left': '60px'
        }

input_style_date = {
        'margin-top': '14px'
        ,'margin-botton': '14px'
        #,'height': '10px'
        }

add_gauge_layout = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(
                                        [
                                                html.P('Gauge ID', style=input_style_label)
                                                ,html.P('Plant', style=input_style_label)
                                                ,html.P('Description', style=input_style_label)
                                                ,html.P('Status', style=input_style_label)
                                                ,html.P('Gauge S/N', style=input_style_label)
                                                ,html.P('Asset No.', style=input_style_label)
                                                ,html.P('Model No.', style=input_style_label)
                                                ,html.P('Type', style=input_style_label)
                                                ,html.P('Unit of Meas', style=input_style_label)
                                                ,html.P('Current Location', style=input_style_label)
                                                ,html.P('Supplier Code', style=input_style_label)
                                                ,html.P('Cost', style=input_style_label)                                                
                                                ,html.P('Purchase Date', style=input_style_label)
                                                ,html.P('Manufacturer', style=input_style_label)
                                        ]
                                        ,width = 1.5
                                )
                                ,dbc.Col(
                                        [
                                                dcc.Input(id='gauge-id-input', type = 'text', style=input_style_field)
                                                #,dcc.Input(id='gauge-plant-input', type = 'text', style=input_style_field)
                                                ,dcc.Dropdown(
                                                        id='plant'
                                                        ,options = [{'label': i, 'value': i} for i in ts.plant_names]
                                                        ,placeholder='Select a plant'
                                                        ,multi=True
                                                        ,value=[]
                                                        ,style={'margin-top': '14px','margin-botton': '14px', 'width': '180px'}
                                                )
                                                ,dcc.Input(id='gauge-description-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-status-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-serial-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-asset-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-model-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-type-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-uom-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-location-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-supplier-code-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-cost-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-purchase-date-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-manufacturer-input', type = 'text', style=input_style_field)
                                        ]
                                        ,width=2
                                )
                                ,dbc.Col(
                                        [
                                                
                                                html.P('Label Code', style=input_style_label)
                                                ,html.P('Calibrator', style=input_style_label)
                                                ,html.P('Last Calibration By', style=input_style_label)
                                                ,html.P('Calibration Frequency (Months)', style=input_style_label)
                                                ,html.P('Last Calibration Date', style=input_style_label_date)
                                                ,html.P('Next Due Calibration Date', style=input_style_label_date)
                                                ,html.P('Next R&R Date', style=input_style_label_date)
                                                ,html.P('Last R&R Date', style=input_style_label_date)
                                                ,html.P('Last R&R Result', style=input_style_label)
                                                ,html.P('Resolution', style=input_style_label)
                                                ,html.P('Pos. Tolerance', style=input_style_label)
                                                ,html.P('Neg. Tolerance', style=input_style_label)
                                        ]
                                        ,width = 1.5
                                )
                                ,dbc.Col(
                                        [
                                                
                                                dcc.Input(id='gauge-label-code-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-calibrator-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-last-calibration-by-input', type = 'text', style=input_style_field)
                                                ,dcc.Input(id='gauge-calibration-freq-input', type = 'text', style=input_style_field)
                                                ,dcc.DatePickerSingle(id='gauge-last-calibration-date-input', style=input_style_date)
                                                ,dcc.DatePickerSingle(id='gauge-last-rr-date-input',  style=input_style_date)
                                                ,dcc.DatePickerSingle(id='gauge-next-rr-date-input',  style=input_style_date)
                                                ,dcc.DatePickerSingle(id='gauge-rr-date-input',  style=input_style_date)
                                                ,dcc.Input(id='gauge-last-rr-result-input',  style=input_style_date)
                                                ,dcc.Input(id='gauge-resolution-input', type = 'number', style=input_style_field)
                                                ,dcc.Input(id='gauge-pos-tolerance-input', type = 'number', style=input_style_field)
                                                ,dcc.Input(id='gauge-neg-tolerance-input', type = 'number', style=input_style_field) 
                                        ]
                                        ,width =2 
                                )
                                ,dbc.Col(
                                        [
                                                html.A('Notes')
                                                ,html.Br()
                                                ,dcc.Input(id='gauge-notes-input', size='65', type = 'text', style=input_style_field)
                                        ]
                                )
                        ]
                )
                #,dbc.Row([]) # Notes
                
                



        ]

)

