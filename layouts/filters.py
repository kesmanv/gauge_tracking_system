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
                        {'label': ' Due Soon Only', 'value': 'Yes'},
                    ],
                    value=[]
) 
                    # ,html.Div(
                    #     [
                    #         html.H5('Status')
                    #         ,dcc.Dropdown(
                    #             id='gauge-status'
                    #             ,options = [
                    #                 {'label':'Active (All)', 'value':'Active'}
                    #                 ,{'label':'Due Soon', 'value':'Due Soon'}
                    #                 ,{'label':'Overdue', 'value':'Overdue'}
                    #             ]
                    #             ,placeholder='Select gauge status'
                    #             ,value=[]
                    #         )
                    #     ]
                    # )
                    # ,html.Br()
                    # ,html.Div([html.H5('Days to due date')
                    #         ,dcc.RangeSlider(id='days_to_due-slider'
                    #                 ,min = 15
                    #                 ,max = 90
                    #                 , step = None
                    #                 , marks = {15: '15',
                    #                     30: '30',
                    #                     60: '60',
                    #                     90: '90',                                        
                    #                 }
                    #         , value = [0,90]
                    #         )
                    # ]
                    # )     
]
)