import dash_core_components as dcc 
import dash_bootstrap_components as dbc 
import plotly.graph_objects as go
from database import  transforms

# Gauges due by manufacturer
gauge_due_cal_mfg = dcc.Graph(id='Gauges-due-mfg'
                        ,figure = go.Figure(data=[go.Bar(y=transforms.gauge_by_mfg['Manufacturer']
                                                    , x=transforms.gauge_by_mfg['No. Gauge Due']
                                                    , orientation='h')])
                        )

#Gauges due by type of gauge
# gauge_due_cal_type = dcc.Graph(id='Gauges-due-type'
#                         ,figure = go.Figure(data=[go.Bar(y=transforms.gauge_by_type['Type']
#                                                     , x=transforms.gauge_by_type['No. Gauge Due']
#                                                     , orientation='h')])
#                         )



data=go.Heatmap(
                   z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening']
                   ,xgap=4
                   ,hoverongaps = False)


calendar_fig = dcc.Graph(id='calendar-test', figure=go.Figure(data=data))

