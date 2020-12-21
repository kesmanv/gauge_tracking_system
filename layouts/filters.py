import dash_html_components as html
import dash_core_components as dcc
from database import transforms

# Common filters
common_filters = html.Div(
    [
        html.Div(
            [
                html.H5('Plant(s)')
                ,dcc.Dropdown(
                    id='plant'
                    ,options = [{'label': i, 'value': i} for i in transforms.plant_names]
                    ,placeholder='Select a plant'
                    ,multi=True
                    ,value=[]
                )
            ]
        )
    ]
)

# Gauge-specifc filters
gauge_filters = html.Div([
                    html.Br()
                    ,html.Div(
                        [
                            html.H5('Guage Manufacturer')
                            ,dcc.Dropdown(
                                id='gauge-manufacturer'
                                
                                #,options = [{'label': i, 'value': i} for i in transforms.gauge_manufacturer]
                                ,placeholder='Select gauge manufacturer'
                                ,multi=True
                                ,value=[]
                            )
                        ]
                    )
                    ,html.Br()
                    ,html.Div(
                        [
                            html.H5('Guage Type')
                            ,dcc.Dropdown(
                                id='gauge-type'
                                #,options = [{'label': i, 'value': i} for i in transforms.gauge_types]
                                ,placeholder='Select gauge type'
                                ,multi=True
                                ,value=[]
                            )
                        ]
                    )
                    ,html.Br()
                    ,dcc.Checklist(
                        id='gauge-due-soon'
                        ,options=[
                            {'label': ' Due Soon Only (next 30 days)', 'value': 'Yes'},
                        ],
                        value=['Yes']
                    )
                    ,dcc.Checklist(
                        id='make-gauge-table-editable'
                        ,options=[
                            {'label': ' Allow record editing', 'value': 'Y'},
                        ]
                        ,value=[]
                    )
                    ,html.Br()
                    ,html.Div(id='tb-download-btn')
                    ,html.Div(id='table-updated') 
                        
]
)
