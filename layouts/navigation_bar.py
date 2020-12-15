import dash_bootstrap_components as dbc

nav = dbc.Nav(
    [
        dbc.NavLink("Dashboard", disabled=True, active=True, href="#")
        ,dbc.NavLink("QAS", disabled=True, href="#")
        ,dbc.NavLink("Gauges", href="/")
        ,dbc.NavLink('Raw Material', disabled=True, href='#')
        ,dbc.NavLink('Root Cause Analysis', disabled=True, href="#")
    ]
)