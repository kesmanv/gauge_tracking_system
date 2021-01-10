import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd

from app import app
from apps import gauge_app, raw_material_app, dashboard_app, qas_app



app.layout = html.Div(
    [
        dcc.Location('app-url', refresh=False)
        ,dbc.Nav(
            children = [
                dbc.NavLink("Dashboard", href="/app/dashboard_app")
                ,dbc.NavLink("QAS", href="/app/qas_app")
                ,dbc.NavLink("Gauges", href="/apps/gauge_app")
                ,dbc.NavLink('Raw Material',  href='/apps/raw_material_app')
                #,dbc.NavLink('Root Cause Analysis', disabled=True, href="#")
            ]
        )
        ,html.Div(id='page-content')
    ]
)

@app.callback(
    Output('page-content', 'children')
    ,Input('app-url', 'pathname')
)
def page_content(pathname):
    if pathname =='/apps/gauge_app':
        return gauge_app.layout
    elif pathname=='/apps/raw_material_app':
        return raw_material_app.layout
    elif pathname=='/app/dashboard_app':
        return dashboard_app.layout
    elif pathname=='/app/qas_app':
        return qas_app.layout
    else:
        return dashboard_app.layout


if __name__ == '__main__':
    app.run_server(debug=True)